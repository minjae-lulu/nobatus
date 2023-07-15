import numpy as np
import plotly.graph_objects as go


npy_file_path = "voxelized.npy"
data = np.load(npy_file_path)

data = np.squeeze(data)

print(f"Shape: {data.shape}")

# Count of 0s, 1s, and not 0 or 1
count_0 = np.count_nonzero(data == 0)
count_1 = np.count_nonzero(data == 1)
count_other = np.count_nonzero((data != 0) & (data != 1))

print(f"Number of 0s: {count_0}")
print(f"Number of 1s: {count_1}")
print(f"Number of values not 0 or 1: {count_other}")
