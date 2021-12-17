class MovementRisk:
    def __init__(self) -> None:
        self.bottom = 1000000
        self.left = 10000000
        self.right = 10000000
        self.top = 10000000
    def min_top(self):
        return min(self.bottom, self.left, self.right)
    def min_bottom(self):
        return min(self.top, self.left, self.right)
    def min_left(self):
        return min(self.bottom, self.right, self.top)
    def min_right(self):
        return min(self.bottom, self.left, self.top)
    def get_min(self):
        return min(self.bottom, self.right, self.left, self.top)
    def __repr__(self) -> str:
        return f"{self.bottom}, {self.top}, {self.right}, {self.left}"

def get_min_risk(risk_map):
    movement_risks = [[MovementRisk() for _ in range(len(risk_map[0]))] for _ in range(len(risk_map))]

    movement_risks[0][0].left=0
    movement_risks[0][0].bottom=0
    min_risk = 0
    min_risk_prev = -1
    while min_risk_prev != min_risk:
        min_risk_prev = min_risk
        for y,row in enumerate(risk_map):
            for x,val in enumerate(row):
                if x != 0:
                    movement_risks[y][x].left = movement_risks[y][x-1].min_right() + val
                if y != 0:
                    movement_risks[y][x].bottom = movement_risks[y-1][x].min_top() + val
        for y,row in enumerate(risk_map):
            for x,val in enumerate(row):
                if x != len(row) - 1:
                    movement_risks[y][x].right = movement_risks[y][x+1].min_left() + val
                if y != len(risk_map) - 1:
                    movement_risks[y][x].top = movement_risks[y+1][x].min_bottom() + val
        min_risk = movement_risks[len(movement_risks)-1][len(movement_risks[0])-1].get_min()
        print(f"found path with {min_risk = }")
    return min_risk


with open('day15.txt') as f:
    lines = f.readlines()

orig_risk_map = list()
for line in lines:
    risk_row = list()
    for risk_level in line.rstrip():
        risk_row.append(int(risk_level))
    orig_risk_map.append(risk_row)


print(f"part1: {get_min_risk(orig_risk_map)}")

part2_risk_map = list()

for y in range(5 * len(orig_risk_map)):
    row = list()
    for x in range(5 * len(orig_risk_map[0])):
        new_risk_val = orig_risk_map[y%len(orig_risk_map)][x%len(orig_risk_map[0])] + (y // len(orig_risk_map)) + (x // len(orig_risk_map))
        row.append(new_risk_val)
    part2_risk_map.append(row)

for y in range(5 * len(orig_risk_map)):
    for x in range(5 * len(orig_risk_map[0])):
        if part2_risk_map[y][x] > 9:
            part2_risk_map[y][x] -= 9
        assert part2_risk_map[y][x] <= 9
print(f"part2: {get_min_risk(part2_risk_map)}")
