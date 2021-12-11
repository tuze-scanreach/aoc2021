with open('day10.txt') as f:
    lines = f.readlines()

OPENERS = ['(', '[', '{', '<']
CLOSERS = [')', ']', '}', '>']
PART1_POINTS = {')': 3, ']': 57, '}': 1197, '>': 25137}
PART2_POINTS = {')': 1, ']': 2, '}': 3, '>': 4}

illegal_chars = list()
closing_incomplete_lines = list()
for line in lines:
    brackets = list()
    illegal_detected = False
    for bracket in line.rstrip():
        if bracket in OPENERS:
            brackets.append(bracket)
        else:
            index = OPENERS.index(brackets[-1]) 
            if CLOSERS[index] == bracket:
                _ = brackets.pop()
            else:
                illegal_chars.append(bracket)
                illegal_detected = True
                break
    if not illegal_detected and len(brackets) > 0:
        closing_chars = list()
        for bracket in brackets:
            index = OPENERS.index(bracket)
            closing_chars.append(CLOSERS[index])
        #print(''.join(closing_chars[::-1]))
        closing_incomplete_lines.append(closing_chars[::-1])


part1_score = 0
for char in illegal_chars:
    part1_score += PART1_POINTS[char]
print(f"{part1_score= }")


part2_scores=list()
for closing_chars in closing_incomplete_lines:
    score =0
    for char in closing_chars:
        score *= 5
        score += PART2_POINTS[char]
    part2_scores.append(score)
part2_score = sorted(part2_scores)[int(len(part2_scores)/2)]
print(f"{part2_score= }")
