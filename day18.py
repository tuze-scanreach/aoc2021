from math import ceil


def explode(number):
    no_levels = 0
    last_no = None
    explode_idx = None
    for idx, char in enumerate(number):
        if char == '[':
            no_levels += 1
        elif char == ']':
            no_levels -= 1
        elif no_levels == 5:
            # explode and return
            new_number = number
            first_digit = char
            for digit in number[idx + 1:]:
                if not digit.isdigit():
                    break
                first_digit += digit

            last_no_size_increase = 0
            if last_no is not None:
                new_number = number[:last_no[0]] + f"{last_no[1] + int(first_digit)}" + number[last_no[0] +
                                                                                               len(str(last_no[1])):]
                last_no_size_increase = len(f"{last_no[1] + int(first_digit)}") - len(str(last_no[1]))
            next_no_start_index = number[idx:].find(']') + idx
            for next_no_idx, next_no in enumerate(number[next_no_start_index:]):
                if next_no.isdigit():
                    second_digit = next_no
                    for digit in number[next_no_start_index + next_no_idx + 1:]:
                        if not digit.isdigit():
                            break
                        second_digit += digit
                    idx_digit_char_start = number[idx:].find(',') + idx + 1
                    idx_second_digit_end = number[idx:].find(']') + idx
                    new_number = new_number[:next_no_start_index + next_no_idx +
                                            last_no_size_increase] + f"{int(second_digit) + int(number[idx_digit_char_start:idx_second_digit_end])}" + number[
                                                next_no_start_index + next_no_idx + len(second_digit):]
                    break
            explode_idx = idx
            break
        elif char.isdigit() and (last_no is None or (idx < last_no[0] or idx > (last_no[0] + len(str(last_no[1]))))):
            last_digit = char
            for digit in number[idx + 1:]:
                if not digit.isdigit():
                    break
                last_digit += digit
            last_no = (idx, int(last_digit))
    if explode_idx is not None:
        new_number = new_number[:explode_idx + last_no_size_increase -
                                1] + "0" + new_number[explode_idx + new_number[explode_idx:].find(']') + 1:]
        return True, new_number
    else:
        return False, number


def split(number):
    for idx, char in enumerate(number):
        if char.isdigit():
            full_digit = char
            for digit in number[idx + 1:]:
                if not digit.isdigit():
                    break
                full_digit += digit
            if int(full_digit) > 9:
                split_val = f"[{int(int(full_digit) / 2)},{ceil(int(full_digit)/2)}]"
                return True, number[:idx] + split_val + number[idx + len(full_digit):]
    return False, number


def add(number1, number2):
    sum_num = '[' + number1 + ',' + number2 + ']'
    while True:
        exploded, sum_num = explode(sum_num)
        split_done = False
        if not exploded:
            split_done, sum_num = split(sum_num)
        if not exploded and not split_done:
            return sum_num


def get_magnitude(num):
    if type(num[0]) is int:
        num1 = num[0]
    else:
        num[0] = get_magnitude(num[0])
    if type(num[1]) is int:
        num2 = num[1]
    else:
        num[1] = get_magnitude(num[1])
    num1 = num[0]
    num2 = num[1]
    return (3 * num1 + 2 * num2)


with open('day18.txt') as f:
    lines = f.readlines()

input = list()
for line in lines:
    input.append(line.rstrip())

sum_num = input[0]
for number in input[1:]:
    sum_num = add(sum_num, number)
# print(sum_num)
print(f"part1:{get_magnitude(eval(sum_num))}")

largest_magnitude = 0
for first_candidate in input:
    for second_canditate in input:
        if first_candidate == second_canditate:
            break
        sum_num = add(first_candidate, second_canditate)
        mag = get_magnitude(eval(sum_num))
        if mag > largest_magnitude:
            largest_magnitude = mag
        sum_num = add(second_canditate, first_candidate)
        mag = get_magnitude(eval(sum_num))
        if mag > largest_magnitude:
            largest_magnitude = mag
print(f"part2:{largest_magnitude}")
