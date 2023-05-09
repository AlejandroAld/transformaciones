from PIL import Image
import numpy as np
from util import ejecutar


def rotar_theta(image: np.array, theta: float) -> np.array:
    n, m, c = image.shape
    esquinas = [(0, 0), (0, m - 1), (n - 1, 0), (n - 1, m - 1)]
    cos_theta = np.cos(-theta)
    sin_theta = np.sin(-theta)
    esquinas_new = [(i - n / 2, j - m / 2) for i, j in esquinas]
    esquinas_new = [((cos_theta * i + sin_theta * j + n / 2),
                     (-sin_theta * i + cos_theta * j + n / 2)) for i, j in esquinas_new]
    esquinas = esquinas_new

    p2, p1 = (max([i for i, j in esquinas]), min([i for i, j in esquinas]))
    q2, q1 = (max([j for i, j in esquinas]), min([j for i, j in esquinas]))
    n_new = round(p2 - p1 + 1)
    m_new = round(q2 - q1 + 1)
    new_matrix = np.zeros((n_new, m_new, c), dtype=image.dtype) + 255
    for i in range(n):
        for j in range(m):
            i_trans = i - n//2
            j_trans = j - m//2
            x = round(cos_theta*i_trans + sin_theta*j_trans + n_new//2 - 1)
            y = round(-sin_theta*i_trans + cos_theta*j_trans + m_new//2 - 1)
            for k in range(c):
                new_matrix[x][y][k] = image[i][j][k]
    return new_matrix


def main():
    theta = [18, 58, 86, 106, 140, -18, -58, -86, -106, -140]
    theta_rad = [np.deg2rad(t) for t in theta]
    image = np.array(Image.open('lena.png'))
    for t, rad in zip(theta, theta_rad):
        ejecutar(image, lambda x: rotar_theta(x, rad), str(t))


