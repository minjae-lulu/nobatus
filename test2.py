import numpy as np
import plotly.graph_objects as go
from stl import mesh

# File name here
stl_filename = "C57289014.stl"

# Read the STL using numpy-stl
main_mesh = mesh.Mesh.from_file(stl_filename)

# Generate each coordinate list
x = main_mesh.vectors.reshape(-1, 9)[:, [0, 3, 6]].flatten()
y = main_mesh.vectors.reshape(-1, 9)[:, [1, 4, 7]].flatten()
z = main_mesh.vectors.reshape(-1, 9)[:, [2, 5, 8]].flatten()

# Generate the index list
I = np.arange(0, len(x), 3)
J = np.arange(1, len(y), 3)
K = np.arange(2, len(z), 3)

# Create a 3D figure
fig = go.Figure(data=[go.Mesh3d(x=x, y=y, z=z, i=I, j=J, k=K, color='lightpink', opacity=0.5)])

# Show the 3D figure
fig.show()


