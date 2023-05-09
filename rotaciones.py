from PIL import Image
import numpy as np
from util import ejecutar


def rotate270(image: np.array) -> np.array:
    n, m, c = image.shape
    new_matrix = np.zeros((m, n, c), dtype=image.dtype)
    for i in range(n):
        for j in range(m):
            for k in range(c):
                z = j
                w = n - i - 1
                new_matrix[z][w][k] = image[i][j][k]
    return new_matrix


def rotate180(image: np.array) -> np.array:
    n, m, c = image.shape
    new_matrix = np.zeros((n, m, c), dtype=image.dtype)
    for i in range(n):
        for j in range(m):
            for k in range(c):
                z = n - i - 1
                w = m - j - 1
                new_matrix[z][w][k] = image[i][j][k]
    return new_matrix


def rotate90(image: np.array) -> np.array:
    n, m, c = image.shape
    new_matrix = np.zeros((m, n, c), dtype=image.dtype)
    for i in range(n):
        for j in range(m):
            for k in range(c):
                z = m - j - 1
                new_matrix[z][i][k] = image[i][j][k]
    return new_matrix


def main():
    image = np.array(Image.open('lena.png'))
    funciones = [rotate90, rotate180, rotate270]
    for f in funciones:
        ejecutar(image, f, f.__name__)


