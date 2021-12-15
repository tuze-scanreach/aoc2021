with open('day13.txt') as f:
    lines = f.readlines()

def fold_on_y(matrix, coord):
  for y in range(coord):
    for x in range(len(matrix[0])):
      matrix[y][x] |= matrix[len(matrix) - y - 1][x]
  return matrix[0:coord]

def fold_on_x(matrix, coord):
  new_matrix = list()
  for y in range(len(matrix)):
    for x in range(coord):
      matrix[y][x] |= matrix[y][len(matrix[y]) - 1 - x]
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
print(folds)

for fold in folds:
  if fold[0] == "y":
    matrix = fold_on_y(matrix, fold[1])
  elif fold[0] == "x":
    matrix = fold_on_x(matrix, fold[1])
  else:
    assert(False)

for line in matrix:
  print("".join(["#" if entry == 1 else "." for entry in line]))

