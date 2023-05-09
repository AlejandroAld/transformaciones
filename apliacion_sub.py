from PIL import Image
import numpy as np
from util import ejecutar


# Palomita
def sub_sampling(image: np.array) -> np.array:
    new_matrix = np.zeros((int(image.shape[0]/2), int(image.shape[1]/2), 3), dtype=image.dtype)
    for i in range(0, image.shape[0], 2):
        for j in range(0, image.shape[1], 2):
            for k in range(3):
                new_matrix[int(i/2)][int(j/2)][k] = image[i][j][k]
    return new_matrix


# Palomita
def sub_sampling_media(image: np.array) -> np.array:
    image = image.astype(np.int32)
    new_matrix = np.zeros((int(image.shape[0]/2), int(image.shape[1]/2), 3), dtype=image.dtype)
    for i in range(0, image.shape[0], 2):
        for j in range(0, image.shape[1], 2):
            for k in range(3):
                new_matrix[int(i/2)][int(j/2)][k] = (image[i][j][k] + image[i+1][j][k] + image[i][j+1][k] +
                                                     image[i+1][j+1][k])//4
    return new_matrix


# Palomita
def ampliacion_2x(image: np.array) -> np.array:
    new_matrix = np.zeros((image.shape[0]*2, image.shape[1]*2, 3), dtype=image.dtype)
    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):
            for k in range(3):
                new_matrix[i*2][j*2][k] = image[i][j][k]
                new_matrix[i*2+1][j*2][k] = image[i][j][k]
                new_matrix[i*2][j*2+1][k] = image[i][j][k]
                new_matrix[i*2+1][j*2+1][k] = image[i][j][k]
    return new_matrix


# Palomita
def ampliacion_2x_media(image: np.array) -> np.array:
    image = image.astype(np.int32)
    new_matrix = np.zeros((image.shape[0]*2, image.shape[0]*2, 3), dtype=image.dtype)
    n, m, _ = image.shape
    for j in range(m):
        for i in range(n):
            for k in range(3):
                new_matrix[i*2][j*2][k] = image[i][j][k]
                new_matrix[i*2+1][j*2][k] = (image[i][j][k] + image[i+1][j][k])//2 if i < n-1 else image[i][j][k]
                new_matrix[i*2][j*2+1][k] = (image[i][j][k] + image[i][j+1][k])//2 if j < m-1 else image[i][j][k]
                new_matrix[i*2+1][j*2+1][k] = (image[i][j][k] + image[i+1][j+1][k])//2 if i < n-1 and j < m-1 \
                    else image[i][j][k]

    return new_matrix


def main():
    image = Image.open("lena.png")
    image = np.array(image)
    funciones = [sub_sampling, sub_sampling_media, ampliacion_2x, ampliacion_2x_media]
    for f in funciones:
        ejecutar(image, f, f.__name__)

