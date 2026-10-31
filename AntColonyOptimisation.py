import random
import math

cities = [
(0, 0),
(1, 5),
(5, 2),
(6, 6),
(8, 3)
]

n = len(cities)

ants = 10
iterations = 50

alpha = 1
beta = 2
rho = 0.5
Q = 100

dist = [[0] * n for _ in range(n)]

for i in range(n):
for j in range(n):
if i != j:
dist[i][j] = math.dist(cities[i], cities[j])

pheromone = [[1.0 if i != j else 0.0 for j in range(n)] for i in range(n)]

best_route = None
best_distance = float('inf')

for iteration in range(iterations):

routes = []

for ant in range(ants):

route = [random.randrange(n)]

while len(route) < n:

current = route[-1]

unvisited = [j for j in range(n) if j not in route]

weights = [
(pheromone[current][j] ** alpha) *
((1 / dist[current][j]) ** beta)
for j in unvisited
]

next_city = random.choices(
unvisited, weights=weights, k=1
)[0]

route.append(next_city)

distance = sum(
dist[route[i]][route[i + 1]]
for i in range(n - 1)
)

distance += dist[route[-1]][route[0]]

routes.append((route, distance))

if distance < best_distance:
best_distance = distance
best_route = route.copy()

for i in range(n):
for j in range(n):
pheromone[i][j] *= (1 - rho)

for route, distance in routes:

deposit = Q / distance

for k in range(n):
a = route[k]
b = route[(k + 1) % n]

pheromone[a][b] += deposit
pheromone[b][a] += deposit

print("Best Route:", [chr(65 + i) for i in best_route])
print("Shortest Distance:", best_distance)
