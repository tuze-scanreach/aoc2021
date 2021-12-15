with open('day13.txt') as f:
    lines = f.readlines()

def fold_on_y(matrix, coord):
  for x in range(len(matrix[0])):
      assert(matrix[coord][x] == 0)
  start_y= coord - (len(matrix) - coord - 1)
  for y in range(start_y, coord):
    for x in range(len(matrix[0])):
      matrix[y][x] |= matrix[len(matrix) - 1 - (y - start_y)][x]
  return matrix[0:coord]

def fold_on_x(matrix, coord):
  new_matrix = list()
  start_x = coord - (len(matrix[0]) - coord - 1)
  for y in range(len(matrix)):
    for x in range(start_x, coord):
      assert(matrix[y][coord] == 0)
      matrix[y][x] |= matrix[y][len(matrix[y]) - 1 - (x - start_x)]
    new_matrix.append(matrix[y][0:coord])
  return new_matrix

xcoord = list()
ycoord = list()
fold_index=0
for fold_index,line in enumerate(lines):
  if line == "\n":
    break
  xcoord.append(int(line.rstrip().split(",")[0]))
  ycoord.append(int(line.rstrip().split(",")[1]))

folds = list()
for index in range(fold_index+1, len(lines)):
  fold_info = lines[index].rstrip().split()[2]
  folds.append((fold_info.split("=")[0], int(fold_info.split("=")[1])))



matrix = [[0] * (max(xcoord)+1) for _ in range(max(ycoord)+1)]

for x,y in zip(xcoord, ycoord):
  matrix[y][x] = 1

first_fold = folds.pop(0)
if first_fold[0] == "y":
  matrix = fold_on_y(matrix, first_fold[1])

if first_fold[0] == "x":
  matrix = fold_on_x(matrix, first_fold[1])

no_dots=0
for line in matrix:
  for dot in line:
    no_dots += dot

print(f"part1: {no_dots}")

for fold in folds:
  if fold[0] == "y":
    matrix = fold_on_y(matrix, fold[1]).copy()
  elif fold[0] == "x":
    matrix = fold_on_x(matrix, fold[1]).copy()
  else:
    assert(False)
print("part2: ")
for line in matrix:
  print("".join(["#" if entry == 1 else "." for entry in line]))

