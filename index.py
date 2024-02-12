import numpy as np
import cv2
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import os
from mesh_utils import create_mesh, scale_mesh

image_path = 'XXXX'
image_name = os.path.splitext(os.path.basename(image_path))[0]
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# 画像のサイズを取得
height, width = image.shape

# 画像をリサイズ
resized_image = cv2.resize(image, (width // 2, height // 2), interpolation=cv2.INTER_AREA)

# 画像を正規化して輝度値を0から1の範囲に変換
normalized_image = resized_image / 255.0

# 高さ情報の変換（黒を厚く、白を薄く）
height_map = 5 * (1 - normalized_image) + 1

# 3Dプロット用のグリッドを生成
x = np.arange(height_map.shape[1])
y = np.arange(height_map.shape[0])
x, y = np.meshgrid(x, y)

# 3Dプロット
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, height_map, cmap='gray')

image_mesh = create_mesh(height_map)

# 生成されたメッシュを指定されたサイズにスケーリング
scale_mesh(image_mesh, 89, 127)

image_mesh.save( image_name + '.stl')

plt.show()