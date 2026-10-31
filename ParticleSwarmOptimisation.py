import random

def fitness(x):
return x * (10 - x)

n = 20
iterations = 50

w = 0.7
c1 = 1.5
c2 = 1.5

positions = [random.uniform(0, 10) for _ in range(n)]
velocities = [random.uniform(-1, 1) for _ in range(n)]

pbest = positions.copy()
gbest = max(pbest, key=fitness)

for _ in range(iterations):

for i in range(n):

r1 = random.random()
r2 = random.random()

velocities[i] = (
w * velocities[i]
+ c1 * r1 * (pbest[i] - positions[i])
+ c2 * r2 * (gbest - positions[i])
)

positions[i] += velocities[i]
positions[i] = max(0, min(10, positions[i]))

if fitness(positions[i]) > fitness(pbest[i]):
pbest[i] = positions[i]

gbest = max(pbest, key=fitness)

print("Best Solution:", gbest)
print("Maximum Fitness:", fitness(gbest))
