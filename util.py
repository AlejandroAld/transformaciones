from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def ejecutar(imagen: np.array, funcion: callable, name: str) -> np.array:
    new = funcion(imagen)
    plt.imshow(new)
    plt.title(name)
    plt.xticks([])
    plt.yticks([])
    plt.show()
    new = Image.fromarray(new.astype(np.uint8))
    new.save("results/lena_" + name + ".png")

