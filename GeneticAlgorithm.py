import random

def fitness(x):
return x * (10 - x)

population = [random.uniform(0, 10) for _ in range(20)]

for generation in range(50):
new_population = []

while len(new_population) < 20:
p1 = max(random.sample(population, 3), key=fitness)
p2 = max(random.sample(population, 3), key=fitness)

child = (p1 + p2) / 2

if random.random() < 0.1:
child += random.uniform(-1, 1)

child = max(0, min(10, child))
new_population.append(child)

population = new_population

best = max(population, key=fitness)

print("Best Solution:", best)
print("Maximum Fitness:", fitness(best))
