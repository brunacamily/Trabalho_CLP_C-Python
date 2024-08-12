# Trabalho de Conceitos de Linguagem de Programação (CLP) 
Repositório contendo o trabalho da disciplina de CLP, com implementação e visualização gráfica utilizando duas linguagens de programação.

## Alunos
    Bruna Novack // bcdnovack@inf.ufpel.edu.br
    Vitor Colombo // vmcolombo@inf.ufpel.edu.br

## Especificação do Trabalho
Implementar uma aplicação gráfica (sugestão: fractal de Mandelbrot, ray tracing, simulação de partículas) com o apoio de duas linguagens de programação: Python e C (ou C++). O desafio consiste em utilizar essas duas linguagens em conjunto, com Python sendo usado para oferecer uma interface com o usuário e apresentar a imagem gerada, enquanto a linguagem C (ou C++) será utilizada para implementar o serviço de cálculo desejado.

## Abordagem Escolhida

A aplicação escolhida foi o fractal de Mandelbrot. Para integrar as linguagens, optamos por uma biblioteca compartilhada. Os passos são:
1. Criar um arquivo em C com as funções para gerar o fractal de Mandelbrot;
2. Compilar o arquivo C e gerar a biblioteca que será usada;
3. Criar um arquivo Python que chama a biblioteca C e gera o gráfico. Adicionalmente, criamos uma pequena interface com botões que permitem escolher o intervalo de visualização do gráfico, mudar as cores ou gerar automaticamente o gráfico.

## Organização dos Arquivos
Na pasta AppFractal estão os seguintes arquivos:
   - `calculo.c`: Contém duas funções para calcular o fractal de Mandelbrot. A partir deste arquivo, será criada a biblioteca compartilhada (`calculo.so`);
   - `calculo.so`: Biblioteca compartilhada usada em Python;
   - `app_interface.py`: Arquivo que gera uma interface e plota um gráfico com o fractal de Mandelbrot;
   - `Makefile`: Pode ser usado para automatizar a compilação e execução do trabalho.

## Bibliotecas Necessárias
- numpy
- matplotlib

## Execução Utilizando Makefile
Abra um terminal Linux ou com suporte para o comando 'make', e execute a seguinte sequência de comandos:
    
- `make`
    
- `make run`

## Execução Passo a Passo Sem Utilizar Makefile
Linux: 
   - Abra o terminal;
   - Navegue até a pasta que contém os arquivos (AppFractal);
   - Execute o comando: `gcc -shared -o calculo.so -fPIC calculo.c` (O comando `gcc -shared -o calculo.so -fPIC calculo.c` compila o arquivo `calculo.c` em uma biblioteca compartilhada chamada `calculo.so`, que pode ser usada por programas que precisam acessar as funções definidas em `calculo.c`).
   - Execute o arquivo Python (`app_interface.py`): `python app_interface.py`.

## Como Funciona a Interface Gráfica
Após a execução, será gerada uma interface gráfica com três botões:
1. **Calcular automaticamente**: O gráfico é gerado imediatamente.
2. **Inserir Parâmetros Manualmente**: Os intervalos de x e y do plano cartesiano são solicitados e, ao final, o gráfico é gerado.
3. **Modificar Coloração Aleatoriamente**: Para modificar as cores, clique neste botão e escolha uma das opções anteriores.