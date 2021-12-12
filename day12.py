
class Cave:
    def __init__(self, isBig, name) -> None:
        self.isBig=isBig
        self.name=name
        self.connections = list()

    def addConnection(self, connection):
        self.connections.append(connection)
    
    def __repr__(self):
        return f"{self.name}"
    
    def __eq__(self, other):
        return self.name == other.name

def getPossibleRoutes(caves, path, current_cave):
    if current_cave.name == "end":
        path.append(current_cave)
        return [path]
    possibilities = list()
    for next_cave in current_cave.connections:
        if not next_cave.isBig and next_cave in path:
            continue
        new_path = path.copy()
        new_path.append(current_cave)
        possibilities.extend(getPossibleRoutes(caves, new_path, next_cave))
    return possibilities


def getPossibleRoutesPart2(caves, path, current_cave):
    if current_cave.name == "end":
        path[1].append(current_cave)
        return [path]
    possibilities = list()
    for next_cave in current_cave.connections:
        isDuplicateSmall = path[0]
        if not next_cave.isBig and next_cave in path[1]:
            if not isDuplicateSmall and next_cave.name not in ["start", "end"]:
                isDuplicateSmall = True
            else:
                continue
        new_path = (isDuplicateSmall, path[1].copy())
        new_path[1].append(current_cave)
        possibilities.extend(getPossibleRoutesPart2(caves, new_path, next_cave))
    return possibilities

with open('day12.txt') as f:
    lines = f.readlines()

cave_names = set()
for line in lines:
    for cave_name in line.rstrip().split('-'):
        cave_names.add(cave_name)

caves = dict()
for cave_name in cave_names:
    cave = Cave(cave_name.isupper(),cave_name)
    caves[cave_name] = cave

for line in lines:
    cave_pair = line.rstrip().split('-')
    caves[cave_pair[0]].addConnection(caves[cave_pair[1]])
    caves[cave_pair[1]].addConnection(caves[cave_pair[0]])

possible_routes = getPossibleRoutes(caves, [], caves["start"])
print(f"part1: {len(possible_routes)}")
possible_routes = getPossibleRoutesPart2(caves, (False,[]), caves["start"])
print(f"part2: {len(possible_routes)}")

