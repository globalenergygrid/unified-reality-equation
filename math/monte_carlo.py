import numpy as np
p = 1e-37 * 0.04 * 1e-5 * 2.5e-43 * 1e-120
trials = int(1e12)  # 1 trillion trials
hits = np.random.random(trials) < p
print(f"Trials: {trials:,} | Hits: {hits.sum()} | Probability: {p:.2e}")
