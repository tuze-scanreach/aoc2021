
class Octopus:
    def __init__(self, energy) -> None:
        self.energy = energy
        self.neighbours = list()

    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)
        assert len(self.neighbours) <= 8
    
    def bump_energy_level(self):
        self.energy += 1
        no_flashes = 0
        if self.energy == 10:
            no_flashes += 1
            for neighbour in self.neighbours:
                no_flashes += neighbour.bump_energy_level()
        return no_flashes
    def clear_maxed_out_energy(self):
        if self.energy >= 10:
            self.energy = 0

    def __repr__(self):
        return str(self.energy)

with open('day11.txt') as f:
    lines = f.readlines()

octopi_matrix = list()
for line in lines:
    octopi = list()
    for octopus_energy in line.rstrip():
        octopi.append(Octopus(int(octopus_energy)))
    octopi_matrix.append(octopi)

for y,octopi in enumerate(octopi_matrix):
    for x,octopus in enumerate(octopi):
        if x + 1 < len(octopi):
            octopus.add_neighbour(octopi_matrix[y][x+1])
        if x - 1 >= 0:
            octopus.add_neighbour(octopi_matrix[y][x-1])
        if y + 1 < len(octopi_matrix):
            octopus.add_neighbour(octopi_matrix[y + 1][x])
            if x + 1 < len(octopi):
                octopus.add_neighbour(octopi_matrix[y + 1][x + 1])
            if x - 1 >= 0:
                octopus.add_neighbour(octopi_matrix[y + 1][x - 1])
        if y - 1 >= 0:
            octopus.add_neighbour(octopi_matrix[y-1][x])
            if x + 1 < len(octopi):
                octopus.add_neighbour(octopi_matrix[y - 1][x + 1])
            if x - 1 >= 0:
                octopus.add_neighbour(octopi_matrix[y - 1][x - 1])
# print(octopi_matrix)

NO_STEPS = 100
no_flashes = 0
MAX_FLASHES_IN_A_STEP = len(octopi_matrix) * len(octopi_matrix[0])
first_step_with_all_flashing = -1
for step_no in range(NO_STEPS):
    no_flashes_in_current_step = 0
    for octopi in octopi_matrix:
        for octopus in octopi:
            no_flashes_in_current_step += octopus.bump_energy_level()
            if no_flashes_in_current_step == MAX_FLASHES_IN_A_STEP:
                first_step_with_all_flashing = step_no
    for octopi in octopi_matrix:
        for octopus in octopi:
            octopus.clear_maxed_out_energy()
    no_flashes += no_flashes_in_current_step

# print(octopi_matrix)
print(f"part1: {no_flashes}")

step_no = NO_STEPS
while(first_step_with_all_flashing < 0):
    no_flashes_in_current_step = 0
    step_no += 1
    for octopi in octopi_matrix:
        for octopus in octopi:
            no_flashes_in_current_step += octopus.bump_energy_level()
    if no_flashes_in_current_step == MAX_FLASHES_IN_A_STEP:
        first_step_with_all_flashing = step_no
        break
    for octopi in octopi_matrix:
        for octopus in octopi:
            octopus.clear_maxed_out_energy()

print(f"part2: {step_no}")
