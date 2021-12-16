from collections import defaultdict
import sys

def get_new_polymer_iterative(rules, polymer):
    new_polymer = polymer[0]
    for i in range(len(polymer) -1):
        key = polymer[i:i+2]
        new_polymer += rules[key] + polymer[i+1]
    return new_polymer

with open('day14.txt') as f:
    lines = f.readlines()

polymer = lines[0].rstrip()
rules = {}
for line in lines[2:]:
    rule = line.rstrip().split(" -> ")
    rules[rule[0]] = rule[1]

NO_STEPS=40
print(f"{NO_STEPS= }")
characters = defaultdict(lambda:0)
if NO_STEPS < 15:
    for step in range(NO_STEPS):
        new_polymer = polymer[0]
        for i in range(len(polymer) -1):
            key = polymer[i:i+2]
            new_polymer += rules[key] + polymer[i+1]
        polymer = new_polymer

    for char in polymer:
        characters[char] += 1
else: 
    # Number of steps is too large
    # do not build the new polymer but keep a count of atom pairs instead
    pair_count = defaultdict(lambda:0)
    for i in range(len(polymer) -1):
        pair_count[polymer[i:i+2]] += 1

    for step in range(NO_STEPS):
        pair_count_start = pair_count.copy()
        for pair in pair_count_start:
            assert pair_count_start[pair] > 0
            new_polymer = rules[pair]
            pair_count[pair] -= pair_count_start[pair]
            if pair_count[pair] == 0:
                pair_count.pop(pair)
            pair_count[pair[0] + new_polymer] += pair_count_start[pair]
            pair_count[new_polymer + pair[1]] += pair_count_start[pair]

    for pair in pair_count:
        characters[pair[0]] += pair_count[pair]
        characters[pair[1]] += pair_count[pair]

    for character in characters:
        characters[character] = int(characters[character] / 2)

    characters[polymer[0]] += 1
    characters[polymer[-1]] += 1

most_common_occurence = 0
least_common_occurence = 10000000000000

for char in characters:
    if characters[char] > most_common_occurence:
        most_common_occurence = characters[char]
    if characters[char] < least_common_occurence:
        least_common_occurence = characters[char]

print(f"{most_common_occurence - least_common_occurence= }")

