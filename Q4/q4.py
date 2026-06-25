import numpy as np

np.random.seed(42)

N = 1_000_000

lam = 10
p = 0.4

N_eggs = np.random.poisson(lam, N)

X_hatch = np.random.binomial(N_eggs, p)
Y_no_hatch = N_eggs - X_hatch

var_diff_sim = np.var(X_hatch - Y_no_hatch)
var_diff_theory = lam

print("Question 4")

print(f"Simulation = {var_diff_sim:.5f}")
print(f"Theory     = {var_diff_theory:.5f}")
