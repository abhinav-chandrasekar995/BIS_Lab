import numpy as np

n = 10
iterations = 50
dim = 1
lb = -10
ub = 10

wolves = np.random.uniform(lb, ub, (n, dim))

def fitness(x):
    return np.sum(x**2)

for t in range(iterations):

    scores = np.array([fitness(w) for w in wolves])
    sorted_indices = np.argsort(scores)

    alpha = wolves[sorted_indices[0]].copy()
    beta = wolves[sorted_indices[1]].copy()
    delta = wolves[sorted_indices[2]].copy()

    a = 2 - 2 * t / iterations

    for i in range(n):

        r1 = np.random.rand(dim)
        r2 = np.random.rand(dim)
        A1 = 2 * a * r1 - a
        C1 = 2 * r2
        D1 = abs(C1 * alpha - wolves[i])
        X1 = alpha - A1 * D1

        r1 = np.random.rand(dim)
        r2 = np.random.rand(dim)
        A2 = 2 * a * r1 - a
        C2 = 2 * r2
        D2 = abs(C2 * beta - wolves[i])
        X2 = beta - A2 * D2

        r1 = np.random.rand(dim)
        r2 = np.random.rand(dim)
        A3 = 2 * a * r1 - a
        C3 = 2 * r2
        D3 = abs(C3 * delta - wolves[i])
        X3 = delta - A3 * D3

        wolves[i] = (X1 + X2 + X3) / 3
        wolves[i] = np.clip(wolves[i], lb, ub)

scores = np.array([fitness(w) for w in wolves])
best_index = np.argmin(scores)

print("Best Solution:", wolves[best_index])
print("Minimum Fitness:", scores[best_index])
