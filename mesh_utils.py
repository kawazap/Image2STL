from stl import mesh
import numpy as np

# 高さマップを基にメッシュを生成する関数
def create_mesh(height_map, scale_factor=1):
    width, height = height_map.shape
    # メッシュの頂点数
    num_tiles = (width - 1) * (height - 1)
    # STLメッシュの作成
    m = mesh.Mesh(np.zeros(num_tiles * 2, dtype=mesh.Mesh.dtype))

    # メッシュの頂点を設定
    for x in range(width - 1):
        for y in range(height - 1):
            z1 = height_map[x][y] * scale_factor
            z2 = height_map[x+1][y] * scale_factor
            z3 = height_map[x][y+1] * scale_factor
            z4 = height_map[x+1][y+1] * scale_factor

            # 1つ目の三角形
            m.vectors[2 * (x * (height - 1) + y)] = np.array([[x, y, z1], [x+1, y, z2], [x, y+1, z3]])
            # 2つ目の三角形
            m.vectors[2 * (x * (height - 1) + y) + 1] = np.array([[x+1, y, z2], [x+1, y+1, z4], [x, y+1, z3]])

    return m

def scale_mesh(mesh, target_width_mm, target_height_mm):
    # メッシュの現在の最大サイズを計算
    current_max_x = np.max(mesh.vectors[:,:,0])
    current_max_y = np.max(mesh.vectors[:,:,1])

    # スケーリング係数を計算
    scale_x = target_width_mm / current_max_x
    scale_y = target_height_mm / current_max_y
    
    # メッシュの全頂点をスケーリング
    mesh.vectors[:,:,0] *= scale_x
    mesh.vectors[:,:,1] *= scale_y