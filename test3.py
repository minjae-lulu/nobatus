import numpy as np
import trimesh
import pyvista as pv
from pyvista import examples
import matplotlib.pyplot as plt
from skimage.measure import marching_cubes

# STL 파일을 읽습니다
mesh = trimesh.load_mesh("C57289014.stl")

# STL 메쉬를 voxel grid로 변환합니다.
# Voxel grid의 해상도는 0.1로 설정했습니다.
# 해상도는 필요에 따라 조정할 수 있습니다.
voxels = mesh.voxelized(pitch=0.05)

# voxel grid를 numpy array로 변환합니다.
array = voxels.matrix

# 저장하려면 이 numpy array를 저장하면 됩니다.
np.save('voxelized.npy', array)
print(array)
# 시각화를 위해 voxel grid를 다시 mesh로 변환합니다.
mesh2 = voxels.marching_cubes

# Pyvista mesh로 변환합니다.
pv_mesh = pv.wrap(mesh2)

# Plotting
p = pv.Plotter()
p.add_mesh(pv_mesh, color=True, show_edges=True, lighting=True)
p.show_grid(color='black')
p.show()
