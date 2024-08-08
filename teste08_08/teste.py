import numpy as np
import matplotlib.pyplot as plt
from ctypes import CDLL, POINTER, c_int, c_double

# Carregar a biblioteca C
mandelbrot = CDLL('./teste.dll')

# Definir os tipos de argumento e retorno da função generate_mandelbrot
mandelbrot.generate_mandelbrot.argtypes = [c_int, c_int, c_double, c_double, c_double, c_double, c_int, POINTER(c_int)]

# Parâmetros do fractal
width, height = 800, 800
x_min, x_max = -2.0, 1.0
y_min, y_max = -1.5, 1.5
max_iter = 1000

# Array para armazenar os resultados
output = np.zeros((height, width), dtype=np.int32)

# Chamar a função C
mandelbrot.generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter, output.ctypes.data_as(POINTER(c_int)))

# Plotar o fractal
plt.imshow(output, extent=(x_min, x_max, y_min, y_max), cmap='hot')
plt.colorbar()
plt.title("Fractal de Mandelbrot")
plt.show()
