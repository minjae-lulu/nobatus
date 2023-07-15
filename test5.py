import numpy as np
import trimesh
from scipy import ndimage

# STL 파일을 읽습니다
mesh = trimesh.load_mesh("C57289014.stl")

# STL 메쉬를 voxel grid로 변환합니다.
voxels = mesh.voxelized(pitch=0.05)

# voxel grid를 numpy array로 변환합니다.
array = voxels.matrix

print(f'Original shape: {array.shape}')  # 변환 전 shape 출력
# 1의 개수를 세어서 출력합니다
num_ones = np.count_nonzero(array)
print(f'Number of 1s: {num_ones}')

# 0의 개수를 세어서 출력합니다
num_zeros = array.size - num_ones
print(f'Number of 0s: {num_zeros}')

# 각 차원에 대한 증가 비율을 계산합니다.
zoom_ratio = np.array([64, 64, 64]) / array.shape
# 선형 보간을 사용하여 배열 크기를 변경합니다.
resized_array = ndimage.zoom(array, zoom_ratio, order=0) # k mean clustering


print(f'Resized shape: {resized_array.shape}') 
num_ones = np.count_nonzero(resized_array)
print(f'Number of 1s: {num_ones}')
num_zeros = resized_array.size - num_ones
print(f'Number of 0s: {num_zeros}')


# npy 파일로 저장합니다
np.save('voxelized.npy', resized_array)
