import numpy as np

np.random.seed(42)

N = 1_000_000

X = np.random.uniform(0, 1, N)
Y = np.random.uniform(0, 1, N)

M = np.maximum(X, Y)
L = np.minimum(X, Y)

mean_M_sim = np.mean(M)
mean_L_sim = np.mean(L)

mean_M_theory = 2 / 3
mean_L_theory = 1 / 3

print("Question 2")

print(f"E[M] Simulation = {mean_M_sim:.5f}")
print(f"E[M] Theory     = {mean_M_theory:.5f}")

print()

print(f"E[L] Simulation = {mean_L_sim:.5f}")
print(f"E[L] Theory     = {mean_L_theory:.5f}")
