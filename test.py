

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from stl import mesh

# File name here
stl_filename = "LVZB011.stl"

# Read the STL using numpy-stl
main_mesh = mesh.Mesh.from_file(stl_filename)

# Create a new plot
figure = plt.figure()
axes = mplot3d.Axes3D(figure)

# Create vertices for each triangle
faces = Poly3DCollection(main_mesh.vectors, linewidths=1, edgecolors='r', alpha=.25)

# Add collection to axes
axes.add_collection3d(faces)

# Auto scale to the mesh size
scale = main_mesh.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)

# Save and display
plt.savefig("3d_model.png")
plt.show()
