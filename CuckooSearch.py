import random
import math

random.seed(10)

def fitness(x):
return x * x

n = 25
iterations = 100
pa = 0.25
beta = 1.5

sigma = (
math.gamma(1 + beta) * math.sin(math.pi * beta / 2) /
(math.gamma((1 + beta) / 2) * beta * 2 ** ((beta - 1) / 2))
) ** (1 / beta)

nests = [random.uniform(-10, 10) for _ in range(n)]

best = min(nests, key=fitness)

for _ in range(iterations):

for i in range(n):

u = random.gauss(0, sigma)
v = random.gauss(0, 1)

step = u / (abs(v) ** (1 / beta))

candidate = nests[i] + 0.1 * step

candidate = max(-10, min(10, candidate))

if fitness(candidate) < fitness(nests[i]):
nests[i] = candidate

ranked = sorted(
range(n),
key=lambda i: fitness(nests[i]),
reverse=True
)

for i in ranked[:int(pa * n)]:
nests[i] = random.uniform(-10, 10)

current = min(nests, key=fitness)

if fitness(current) < fitness(best):
best = current

print("Best Solution:", best)
print("Minimum Fitness:", fitness(best))
