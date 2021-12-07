with open('day6.txt') as f:
    lines = f.readlines()

start_population = list()
for num in lines[0].split(','):
    start_population.append(int(num))


# Brute force with hopeless optimizations
population = start_population.copy()
NO_DAYS_TO_SIMULATE = 80
day_no = 0
while True:
    step = min(6, NO_DAYS_TO_SIMULATE - day_no)
    day_no += step
    for i in range(len(population)):
        population[i] -= step
        if population[i] < 0:
            population.append(9+population[i])
            population[i] += 7
    if day_no == NO_DAYS_TO_SIMULATE:
        break

print(f"{NO_DAYS_TO_SIMULATE= }")
print(len(population))


# Grouping based on age
NO_DAYS_TO_SIMULATE = 256
ages = [0] * 9
for age in start_population:
    ages[age] += 1

for day in range(NO_DAYS_TO_SIMULATE):
        birther_count = ages[0]
        for i in range(0, len(ages)-1):
            ages[i] = ages[i+1]
        ages[6] += birther_count
        ages[8] = birther_count

print(f"{NO_DAYS_TO_SIMULATE= }")
print(sum(ages))

