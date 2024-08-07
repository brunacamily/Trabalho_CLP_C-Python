import numpy as np
import matplotlib.pyplot as plt
import ctypes

# Carrega a biblioteca C
lib = ctypes.CDLL('./teste.so')

# Define o tipo de retorno da função mandelbrot
lib.mandelbrot.restype = ctypes.c_int

# Define os parâmetros da função mandelbrot
lib.mandelbrot.argtypes = [ctypes.c_double, ctypes.c_double]

def calcular_mandelbrot(largura, altura, x_min, x_max, y_min, y_max):
    # Cria uma grade de números complexos
    x = np.linspace(x_min, x_max, largura)
    y = np.linspace(y_min, y_max, altura)
    Z = np.zeros((altura, largura), dtype=int)

    for i in range(altura):
        for j in range(largura):
            # Chama a função mandelbrot da biblioteca C
            iter = lib.mandelbrot(x[j], y[i])
            Z[i, j] = iter

    return Z

def plotar_mandelbrot(Z):
    plt.imshow(Z, extent=(-2, 1, -1.5, 1.5), cmap='hot', interpolation='bilinear')
    plt.colorbar()
    plt.title("Conjunto de Mandelbrot")
    plt.xlabel("Parte Real")
    plt.ylabel("Parte Imaginária")
    plt.show()

# Parâmetros da imagem
largura = 800
altura = 800
x_min, x_max = -2, 1
y_min, y_max = -1.5, 1.5

# Gera a imagem do conjunto de Mandelbrot
Z = calcular_mandelbrot(largura, altura, x_min, x_max, y_min, y_max)

# Plota a imagem
plotar_mandelbrot(Z)
