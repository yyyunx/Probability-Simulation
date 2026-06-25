import numpy as np

np.random.seed(42)

N = 1_000_000

rolls = np.random.multinomial(13, [1/6] * 6, size=N)

N1 = rolls[:, 0]
N2 = rolls[:, 1]
N5 = rolls[:, 4]
N6 = rolls[:, 5]

print("Question 5")

print(f"(a) Simulation = {np.var(N1):.5f}")
print(f"(a) Theory     = {65/36:.5f}")

print()

print(f"(b) Simulation = {np.var(N1 + N2):.5f}")
print(f"(b) Theory     = {26/9:.5f}")

print()

print(f"(c) Simulation = {np.cov(N1, N2)[0, 1]:.5f}")
print(f"(c) Theory     = {-13/36:.5f}")

print()

print(f"(d) Simulation = {np.cov(N1 + N2, N5 + N6)[0, 1]:.5f}")
print(f"(d) Theory     = {-13/9:.5f}")
