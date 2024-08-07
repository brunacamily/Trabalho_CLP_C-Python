import matplotlib.pyplot as plt
import numpy as np

def mostrar_imagem_ppm(caminho_arquivo):
    # Lê a imagem PPM
    with open(caminho_arquivo, 'r') as arquivo:
        # Lê o cabeçalho
        tipo = arquivo.readline().strip()
        largura, altura = map(int, arquivo.readline().strip().split())
        valor_max = int(arquivo.readline().strip())

        # Lê os dados da imagem
        pixels = []
        for linha in arquivo:
            pixels.extend(map(int, linha.split()))

    # Converte a lista de pixels em um array numpy e redimensiona
    imagem_array = np.array(pixels).reshape((altura, largura, 3))

    # Exibe a imagem
    plt.imshow(imagem_array)
    plt.axis('off')  # Desliga os eixos
    plt.show()

# Exemplo de uso
caminho_arquivo = "mandelbrot.ppm"  # Substitua pelo caminho do seu arquivo PPM
mostrar_imagem_ppm(caminho_arquivo)
