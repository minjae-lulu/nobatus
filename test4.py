import numpy as np
import trimesh
import pyvista as pv
from pyvista import examples
import matplotlib.pyplot as plt
from skimage.measure import marching_cubes

# npy 파일을 불러옵니다
array = np.load('voxelized.npy')

# array에서 True의 위치를 찾습니다
coords = np.argwhere(array)

# 특정 threshold 이상의 값을 가진 복셀에 대해 marching cubes 알고리즘을 사용하여 메쉬를 생성합니다
verts, faces, normals, values = marching_cubes(array, level=0)

# Pyvista mesh를 생성합니다
pv_mesh = pv.PolyData(verts, faces)

# Plotting
p = pv.Plotter()
p.add_mesh(pv_mesh, color=True, show_edges=True, lighting=True)
p.show_grid(color='black')
p.show()
