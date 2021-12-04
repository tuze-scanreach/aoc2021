with open('day3.txt') as f:
    numbers = f.readlines()

one_count = len(numbers[0].rstrip()) * [0]
zero_count = len(numbers[0].rstrip()) * [0]

for num in numbers:
    for idx, bit in enumerate(num.rstrip()):
        if bit == '1':
            one_count[idx] += 1
        elif bit == '0':
            zero_count[idx] += 1
        else:
            print(f"{bit=}, {num=}")
            assert(False)

one_count_le = one_count[::-1]
zero_count_le = zero_count[::-1]
gamma = 0
epsilon = 0
for i in range(len(one_count_le)):
    if one_count_le[i] > zero_count_le[i]:
        gamma += 1 << i
    elif one_count_le[i] < zero_count_le[i]:
        epsilon += 1 << i
    else:
        assert(False)

print(f"{epsilon=}, {gamma=}, {epsilon * gamma = }")


o_gen_rating_candidates = numbers.copy()
most_common_val = int(one_count[0] >= zero_count[0])
index = 0

while len(o_gen_rating_candidates) > 1:
    new_candidates = list()
    no_ones_in_next_index = 0
    for candidate in o_gen_rating_candidates:
        if int(candidate[index]) == most_common_val:
            new_candidates.append(candidate)
            if candidate[index + 1] == "1":
                no_ones_in_next_index += 1
    if no_ones_in_next_index >= len(new_candidates)/2:
        most_common_val = 1
    else:
        most_common_val = 0
    index += 1
    o_gen_rating_candidates = new_candidates.copy()

o_gen_rating = int(o_gen_rating_candidates[0].rstrip(), 2)
print(f"{o_gen_rating =}")


co2_scrub_rating_candidates = numbers.copy()
least_common_val = 1 - int(one_count[0] >= zero_count[0])
index = 0

while len(co2_scrub_rating_candidates) > 1:
    new_candidates = list()
    no_ones_in_next_index = 0
    for candidate in co2_scrub_rating_candidates:
        if int(candidate[index]) == least_common_val:
            new_candidates.append(candidate)
            if candidate[index + 1] == "1":
                no_ones_in_next_index += 1
    if no_ones_in_next_index >= len(new_candidates) / 2:
        least_common_val = 0
    else:
        least_common_val = 1
    index += 1
    co2_scrub_rating_candidates = new_candidates.copy()

co2_scrub_rating = int(co2_scrub_rating_candidates[0].rstrip(), 2)
print(f"{co2_scrub_rating =}")

print(f"{o_gen_rating * co2_scrub_rating= }")
