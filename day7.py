import numpy
with open('day7.txt') as f:
    lines = f.readlines()

numbers = [int(x) for x in lines[0].split(",")]
median = numpy.median(numbers)
print(f"part1: {sum([abs(x - median) for x in numbers])}")


mean = round(numpy.mean(numbers))
max_val = max(numbers)
min_val = min(numbers)
distmap = list()
distmap.append(0)
for i in range(1, max_val + 1):
    distmap.append(distmap[i-1] + i)

best_cost = sum([distmap[abs(x-mean)] for x in numbers])
#check before and after too:
new_cost = sum([distmap[abs(x-(mean + 1))] for x in numbers])
if new_cost <= best_cost:
    best_cost = new_cost
new_cost = sum([distmap[abs(x-(mean - 1))] for x in numbers])
if new_cost <= best_cost:
    best_cost = new_cost

print(f"part2: {best_cost =}")

