def position_overshot_given_range(position, target_x_range, target_y_range, velocity):
    overshot = position[0] > target_x_range[1]
    overshot |= position[1] < target_y_range[0] and velocity[1] <= 0
    return overshot


def position_in_given_range(position, target_x_range, target_y_range):
    in_range = position[0] >= target_x_range[0] and position[
        0] <= target_x_range[1]
    in_range &= position[1] >= target_y_range[0] and position[
        1] <= target_y_range[1]
    return in_range


def hits_the_target_range(target_x_range, target_y_range, velocity):
    step_no = 0
    position = [0, 0]
    while True:
        position[0] += velocity[0]
        position[1] += velocity[1]
        if position_in_given_range(position, target_x_range, target_y_range):
            #print(position)
            return True
        if position_overshot_given_range(position, target_x_range, target_y_range, velocity):
            #print(position)
            return False
        velocity[0] = 0 if velocity[0] == 0 else velocity[0] - 1
        velocity[1] -= 1


with open('day17.txt') as f:
    lines = f.readlines()
info = lines[0].split(",")
x_range_info = info[0][info[0].find("x=") + 2:]
x_range_info = x_range_info.split("..")
target_x_range = (int(x_range_info[0]), int(x_range_info[1]))
y_range_info = info[1][info[1].find("y=") + 2:]
y_range_info = y_range_info.split("..")
target_y_range = (int(y_range_info[0]), int(y_range_info[1]))

min_y = target_y_range[0]
max_x = target_x_range[1]
min_x = 0
while True:
    if sum(list(range(min_x + 1))) >= target_x_range[0]:
        break
    min_x += 1
min_no_steps = min_x + 1
max_y = min_no_steps

for i in range(500):
    if hits_the_target_range(target_x_range, target_y_range, [min_x, i]):
        max_y = i
print(f"part1: {sum(list(range(max_y+1)))}")

no_possible_velocities = 0

for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        if hits_the_target_range(target_x_range, target_y_range, [x, y]):
            no_possible_velocities += 1

print(f"part2: {no_possible_velocities}")
