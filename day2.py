with open('day2.txt') as f:
    instructions = f.readlines()

h_loc = 0
v_loc = 0
for instruction in instructions:
    dir = instruction.split()[0]
    if dir == "forward":
        h_loc += int(instruction.split()[1])
    elif dir == "down":
        v_loc += int(instruction.split()[1])
    elif dir == "up":
        v_loc -= int(instruction.split()[1])
    else:
        assert(False)

print(f"part1: {v_loc * h_loc}")

h_loc = 0
v_loc = 0
aim = 0
for instruction in instructions:
    dir = instruction.split()[0]
    if dir == "forward":
        h_loc += int(instruction.split()[1])
        v_loc += aim * int(instruction.split()[1])
    elif dir == "down":
        aim += int(instruction.split()[1])
    elif dir == "up":
        aim -= int(instruction.split()[1])
    else:
        assert(False)

print(f"part2: {v_loc * h_loc}")
