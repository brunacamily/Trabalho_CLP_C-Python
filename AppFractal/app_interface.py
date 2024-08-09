import numpy as np
import matplotlib.pyplot as plt
from ctypes import CDLL, POINTER, c_int, c_double
import tkinter as tk
from tkinter import messagebox, simpledialog
from matplotlib import colormaps
import random

# Carregar a biblioteca C
mandelbrot = CDLL('./calculo.dll')
mandelbrot.generate_mandelbrot.argtypes = [c_int, c_int, c_double, c_double, c_double, c_double, c_int, POINTER(c_int)]

cmap = 'hot'

def set_color():
    global cmap
    colormaps1 = list(colormaps)
    cmap = random.choice(colormaps1)
    
# Função para gerar o fractal de Mandelbrot e plotar o gráfico
def gerar_fractal(auto_mode=True):
    width, height = 800, 800
    
    if auto_mode:
        x_min, x_max = -2.0, 1.0
        y_min, y_max = -1.5, 1.5
        max_iter = 1000
    else:
        while True:
            try:
                max_iter = simpledialog.askinteger("Número de Iterações", "Insira o número de iterações:", minvalue=1)
                if max_iter is None:
                    return

                x_min = simpledialog.askfloat("Dimensão X Mínima", "Insira o valor mínimo de X:")
                if x_min is None:
                    return

                x_max = simpledialog.askfloat("Dimensão X Máxima", "Insira o valor máximo de X:")
                if x_max is None:
                    return

                y_min = simpledialog.askfloat("Dimensão Y Mínima", "Insira o valor mínimo de Y:")
                if y_min is None:
                    return

                y_max = simpledialog.askfloat("Dimensão Y Máxima", "Insira o valor máximo de Y:")
                if y_max is None:
                    return

                break
            except ValueError as e:
                retry = messagebox.askretrycancel("Erro", f"Entrada inválida: {e}")
                if not retry:
                    return

    output = np.zeros((height, width), dtype=np.int32)
    mandelbrot.generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter, output.ctypes.data_as(POINTER(c_int)))

    plt.imshow(output, extent=(x_min, x_max, y_min, y_max), cmap=cmap )
    plt.colorbar()
    plt.title("Fractal de Mandelbrot")
    plt.show()

# Configuração da interface gráfica
def iniciar_interface():
    root = tk.Tk()
    root.title("Gerador de Fractais de Mandelbrot")
    root.geometry("400x300")

    tk.Label(root, text="Escolha como deseja calcular o fractal:", font=("Arial", 12)).pack(pady=20)

    tk.Button(root, text="Calcular Automaticamente", command=lambda: gerar_fractal(auto_mode=True), font=("Arial", 10)).pack(pady=10)
    tk.Button(root, text="Inserir Parâmetros Manualmente", command=lambda: gerar_fractal(auto_mode=False), font=("Arial", 10)).pack(pady=10)

    # Botões de colormap lado a lado
    
    tk.Button(root, text="Modificar coloração aleatoriamente", command=lambda: set_color(), font=("Arial", 10)).pack(pady=10)
    

    # Garantir que fechar a janela principal feche todas as outras janelas
    root.protocol("WM_DELETE_WINDOW", root.quit)

    root.mainloop()

if __name__ == "__main__":
    iniciar_interface()