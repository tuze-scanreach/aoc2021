from collections import defaultdict


with open('day9.txt') as f:
    lines = f.readlines()

def add_to_basin(basin_numbers, basin_number, map, x, y):
    if map[y][x] < 9:
        basin_numbers[(x,y)] = basin_number
        if y - 1 >= 0 and basin_numbers[(x,y-1)] is None:
            add_to_basin(basin_numbers, basin_number, map, x, y-1)
        if y + 1 < len(map) and basin_numbers[(x,y+1)] is None:
            add_to_basin(basin_numbers, basin_number, map, x, y+1)
        if x - 1 >= 0 and basin_numbers[(x-1,y)] is None:
            add_to_basin(basin_numbers, basin_number, map, x - 1, y)
        if x + 1 < len(map[0]) and basin_numbers[(x+1,y)] is None:
            add_to_basin(basin_numbers, basin_number, map, x + 1, y)


map = list()
for row_no, row in enumerate(lines):
    map.append(list())
    for height in row.rstrip():
        map[row_no].append(int(height))

low_points = []
low_point_coords = []
for y in range(0, len(map)):
    for x in range(0, len(map[0])):
        neighbours =  list() #[map[max(y-1, 0)][x], map[y][max(x-1, 0)], map[min(y+1, len(map) -1)][x], map[y][min(x+1, len(map[0])-1)]]
        if y -1 >= 0:
            neighbours.append(map[y-1][x])
        if x -1 >= 0:
            neighbours.append(map[y][x-1])
        if y + 1 < len(map):
            neighbours.append(map[y + 1][x])
        if x + 1 < len(map[0]):
            neighbours.append(map[y][x+1])
        if all([map[y][x] < neighbour_height for neighbour_height in neighbours]):
            low_points.append(map[y][x])
            low_point_coords.append((x,y))

print(f"part1: {sum(low_points) + len(low_points)}")

basin_sizes = [0] * len(low_points)
basin_numbers = defaultdict(lambda:None)
for basin_no,(x,y) in enumerate(low_point_coords):
    add_to_basin(basin_numbers, basin_no, map, x, y)

for i in range(len(basin_sizes)):
    basin_sizes[i] = len([basin_no for basin_no in basin_numbers.values() if basin_no == i])

sorted_basin_sizes = sorted(basin_sizes, reverse=True)
part2_value = 1
for val in sorted_basin_sizes[:3]:
    part2_value *= val

print(f"part2: {part2_value}")

