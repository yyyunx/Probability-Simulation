import numpy as np

np.random.seed(42)

N = 1_000_000

U = np.random.uniform(0,1,N)
W1 = 1-U
W2 = np.random.exponential(1,N)

prob_a_sim = np.mean(W1<W2)
prob_a_theory = 1-np.exp(-1)

cond = W2<=1
prob_b_sim = np.mean(W1[cond]<W2[cond])
prob_b_theory = (np.exp(1)-2)/(np.exp(1)-1)

print("Question 1")
print(f"(a) Simulation = {prob_a_sim:.5f}")
print(f"(a) Theory     = {prob_a_theory:.5f}")

print()

print(f"(b) Simulation = {prob_b_sim:.5f}")
print(f"(b) Theory     = {prob_b_theory:.5f}")
