import numpy as np

np.random.seed(42)

N = 1_000_000

# (a) Exponential(1)
X_exp = np.random.exponential(1, N)
Y_exp = np.random.exponential(1, N)

M_exp = np.maximum(X_exp, Y_exp)
L_exp = np.minimum(X_exp, Y_exp)

cov_exp_sim = np.cov(M_exp, L_exp)[0, 1]
cov_exp_theory = 1 / 4

# (b) Normal(0,1)
X_norm = np.random.normal(0, 1, N)
Y_norm = np.random.normal(0, 1, N)

M_norm = np.maximum(X_norm, Y_norm)
L_norm = np.minimum(X_norm, Y_norm)

cov_norm_sim = np.cov(M_norm, L_norm)[0, 1]
cov_norm_theory = 1 / np.pi

print("Question 3")

print(f"(a) Simulation = {cov_exp_sim:.5f}")
print(f"(a) Theory     = {cov_exp_theory:.5f}")

print()

print(f"(b) Simulation = {cov_norm_sim:.5f}")
print(f"(b) Theory     = {cov_norm_theory:.5f}")
