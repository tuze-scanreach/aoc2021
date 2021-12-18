from construct import version
import numpy as np
import binascii

VERSION_WIDTH = 3
TYPEID_WIDTH = 3
ALIGNMENT = 4
SUM_TYPE = 0
PROD_TYPE = 1
MIN_TYPE = 2
MAX_TYPE = 3
LITERAL_TYPE = 4
GREATER_TYPE = 5
LESS_TYPE = 6
EQUAL_TYPE = 7


class Header:
    def __init__(self, version, typeId) -> None:
        self.version = version
        self.typeId = typeId

    def __repr__(self) -> str:
        return f"ver: {self.version}, tId: {self.typeId}"


class LiteralValue:
    def __init__(self, data) -> None:
        self.no_bits_read = 0
        self.values = list()
        self.value = 0
        more_data = True
        while more_data:
            value = int(data[self.no_bits_read + 1:self.no_bits_read + 5], 2)
            self.values.append(value)
            more_data = data[self.no_bits_read] == '1'
            self.no_bits_read += 5
        for i, val in enumerate(self.values[::-1]):
            self.value |= val << (i * ALIGNMENT)

    def __repr__(self) -> str:
        return f"{self.value}"


class OperatorValue:
    def __init__(self, data) -> None:
        self.length_type = int(data[0])
        self.no_bits_read = 1
        self.packets = list()
        self.subpacket_values = list()
        self.value = None
        if self.length_type == 0:
            self.total_payloadlength = int(data[1:16], 2)
            self.no_sub_packets = 0
            self.no_bits_read += 15
        else:
            self.total_payloadlength = 0
            self.no_sub_packets = int(data[1:12], 2)
            self.no_bits_read += 11
        payload_bits_read = 0
        while payload_bits_read < self.total_payloadlength or len(self.packets) < self.no_sub_packets:
            bits_read, packet = parse_one_whole_packet(data[self.no_bits_read:])
            self.packets.append(packet)
            self.subpacket_values.append(packet.value.value)
            payload_bits_read += bits_read
            self.no_bits_read += bits_read

    def __repr__(self) -> str:
        return f"{self.packets}"


class Packet:
    def __init__(self, header, value) -> None:
        self.header = header
        self.value = value

    def __repr__(self) -> str:
        return f"packet: {self.header}, val: {self.value}"


def greater_than(array):
    assert len(array) == 2
    return int(array[0] > array[1])


def less_than(array):
    assert len(array) == 2
    return int(array[0] < array[1])


def equal(array):
    assert len(array) == 2
    return int(array[0] == array[1])


version_sum = 0


def parse_one_whole_packet(bin_data: str):
    global version_sum
    bits_read = 0
    #print(bin_data[bits_read: bits_read+VERSION_WIDTH])
    version = int(bin_data[bits_read:bits_read + VERSION_WIDTH], 2)
    version_sum += version
    bits_read += VERSION_WIDTH
    typeId = int(bin_data[bits_read:bits_read + TYPEID_WIDTH], 2)
    bits_read += TYPEID_WIDTH
    header = Header(version, typeId)

    if typeId == LITERAL_TYPE:
        value = LiteralValue(bin_data[bits_read:])
    else:
        PACKET_VALUE_CALC_LOOKUP = {
            SUM_TYPE: sum,
            PROD_TYPE: np.prod,
            MIN_TYPE: min,
            MAX_TYPE: max,
            GREATER_TYPE: greater_than,
            LESS_TYPE: less_than,
            EQUAL_TYPE: equal
        }
        value = OperatorValue(bin_data[bits_read:])
        value.value = PACKET_VALUE_CALC_LOOKUP[typeId](value.subpacket_values)
    packet = Packet(header, value)
    bits_read += value.no_bits_read

    #print(f"{bits_read}, {packet}")
    return (bits_read, packet)


def parse_all_packets(bin_data: str):
    packets = list()
    index = 0
    bits_read, packet = parse_one_whole_packet(bin_data[index:])
    print(f"Bits left: {len(bin_data) - bits_read}")


hex_packet = "E058F79802FA00A4C1C496E5C738D860094BDF5F3ED004277DD87BB36C8EA800BDC3891D4AFA212012B64FE21801AB80021712E3CC771006A3E47B8811E4C01900043A1D41686E200DC4B8DB06C001098411C22B30085B2D6B743A6277CF719B28C9EA11AEABB6D200C9E6C6F801F493C7FE13278FFC26467C869BC802839E489C19934D935C984B88460085002F931F7D978740668A8C0139279C00D40401E8D1082318002111CE0F460500BE462F3350CD20AF339A7BB4599DA7B755B9E6B6007D25E87F3D2977543F00016A2DCB029009193D6842A754015CCAF652D6609D2F1EE27B28200C0A4B1DFCC9AC0109F82C4FC17880485E00D4C0010F8D110E118803F0DA1845A932B82E200D41E94AD7977699FED38C0169DD53B986BEE7E00A49A2CE554A73D5A6ED2F64B4804419508B00584019877142180803715224C613009E795E58FA45EA7C04C012D004E7E3FE64C27E3FE64C24FA5D331CFB024E0064DEEB49D0CC401A2004363AC6C8344008641B8351B08010882917E3D1801D2C7CA0124AE32DD3DDE86CF52BBFAAC2420099AC01496269FD65FA583A5A9ECD781A20094CE10A73F5F4EB450200D326D270021A9F8A349F7F897E85A4020CF802F238AEAA8D22D1397BF27A97FD220898600C4926CBAFCD1180087738FD353ECB7FDE94A6FBCAA0C3794875708032D8A1A0084AE378B994AE378B9A8007CD370A6F36C17C9BFCAEF18A73B2028C0A004CBC7D695773FAF1006E52539D2CFD800D24B577E1398C259802D3D23AB00540010A8611260D0002130D23645D3004A6791F22D802931FA4E46B31FA4E4686004A8014805AE0801AC050C38010600580109EC03CC200DD40031F100B166005200898A00690061860072801CE007B001573B5493004248EA553E462EC401A64EE2F6C7E23740094C952AFF031401A95A7192475CACF5E3F988E29627600E724DBA14CBE710C2C4E72302C91D12B0063F2BBFFC6A586A763B89C4DC9A0"
pack_in_list_format = list(binascii.unhexlify(hex_packet))
pack_in_binary_str = "".join(
    np.vectorize(np.binary_repr)(pack_in_list_format, width=8))
bits_read, packet = parse_one_whole_packet(pack_in_binary_str)
print(f"Bits left: {len(pack_in_binary_str) - bits_read}")
print(f"part1: {version_sum}")
print(f"part2: {packet.value.value}")
