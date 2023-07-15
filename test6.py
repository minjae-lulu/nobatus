import numpy as np
import plotly.graph_objects as go

# npy 파일을 불러옵니다
array = np.load('B14120054.npy')

# 좌표를 생성합니다
x, y, z = np.mgrid[:array.shape[0], :array.shape[1], :array.shape[2]]

# 값이 1인 점만 선택합니다
x = x[array > 0]
y = y[array > 0]
z = z[array > 0]

# 3D scatter plot을 생성합니다
fig = go.Figure(data=go.Scatter3d(
    x=x, y=y, z=z,
    mode='markers',
    marker=dict(
        size=4,
        color=z,                # 데이터에 따라 색상을 변경합니다
        colorscale='Viridis',    # 특정 색상 스케일을 선택합니다
        opacity=0.8
    )
))

fig.update_layout(margin=dict(r=20, l=10, b=10, t=10))

fig.show()
