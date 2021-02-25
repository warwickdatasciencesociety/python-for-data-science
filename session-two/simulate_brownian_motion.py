"""Brownian motion simulation using a Gaussian random walk."""

import numpy as np
import pandas as pd


# Parameters
T = 1000  # number of timesteps
N = 100  # number of particles

# Generate data
t = np.linspace(0, 1, 1000)
data = {
    'particle': [],
    'time': [],
    'x': [],
    'y': []
}
for i in range(10):
    data['particle'].extend(np.full(t.shape, i+1))
    data['time'].extend(t)
    data['x'].append(0)
    data['x'].extend(np.cumsum(np.random.normal(size=t.shape[0]-1)))
    data['y'].append(0)
    data['y'].extend(np.cumsum(np.random.normal(size=t.shape[0]-1)))

# Export
df = pd.DataFrame(data)
df.to_csv('data/brownian_motion.csv', index=False)
