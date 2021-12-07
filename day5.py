def get_coordinates_from_line(line_txt):
    coordinates = list()
    for coordinate in line_txt.split('->'):
        coordinates.append(
            (int(coordinate.split(',')[0]), int(coordinate.split(',')[1])))
    return coordinates


def line_horizontal(coordinates):
    return coordinates[0][0] == coordinates[1][0]


def line_vertical(coordinates):
    return coordinates[0][1] == coordinates[1][1]


def line_diagonal(coordinates):
    return abs(coordinates[0][1] -
               coordinates[1][1]) == abs(coordinates[0][0] - coordinates[1][0])


with open('day5.txt') as f:
    lines = f.readlines()

MATRIX_SIZE = 1000
PART_2_ON = True
line_matrix = [[0] * MATRIX_SIZE for _ in range(MATRIX_SIZE)]
for line in lines:
    line_coordinates = get_coordinates_from_line(line.rstrip())
    if PART_2_ON and line_diagonal(line_coordinates):
        print(line_coordinates)
        x_step = 1
        from_x = line_coordinates[0][0]
        to_x = line_coordinates[1][0]
        if from_x > to_x:
            x_step = -1
        y_step = 1
        from_y = line_coordinates[0][1]
        to_y = line_coordinates[1][1]
        if from_y > to_y:
            y_step = -1
        for x, y in zip(range(from_x, to_x + x_step, x_step),
                        range(from_y, to_y + y_step, y_step)):
            line_matrix[y][x] += 1
    elif line_horizontal(line_coordinates):
        from_y = min(line_coordinates[0][1], line_coordinates[1][1])
        to_y = max(line_coordinates[0][1], line_coordinates[1][1])
        for i in range(from_y, to_y + 1):
            line_matrix[i][line_coordinates[0][0]] += 1
    elif line_vertical(line_coordinates):
        from_x = min(line_coordinates[0][0], line_coordinates[1][0])
        to_x = max(line_coordinates[0][0], line_coordinates[1][0])
        for i in range(from_x, to_x + 1):
            line_matrix[line_coordinates[0][1]][i] += 1
#print(line_matrix)
no_points_w_overlapping_lines = 0
for row in line_matrix:
    for point in row:
        if point > 1:
            no_points_w_overlapping_lines += 1

print(f"{no_points_w_overlapping_lines= }")
