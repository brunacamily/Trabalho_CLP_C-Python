# Trabalho de Conceitos de Linguagem de Programação (CLP) 
 Repositório contendo trabalho da disciplina de CLP implementação com visualização gráfica e duas linguagens de programação.

## Alunos
    Bruna Novack // bcdnovack@inf.ufpel.edu.br
    Vitor Colombo // vmcolombo@inf.ufpel.edu.br

## Específicação do trabalho
Implementar uma aplicação gráfica (sugestão: fractal de Mandelbrot, ray tracing, simulação de partículas) com apoio de duas linguagens de programação: Python e C (ou C++). O desafio consiste em realizar o uso conjunto de duas linguagens de programação, sendo o desafio especificamente, realizar o uso conjunto das linguagens. Python deve ser utilizado para oferecer uma interface com o usuário e apresentar a imagem gerada. A linguagem C (ou C++) deve ser utilizada para implementar o serviço de cálculo desejado.

## Abordagem escolhida
Visando as exigências estabelecidas escolhemos gerar o fractal de Mandelbrot, para isso 

## Organização dos arquivos
    Na pasta AppFractal contém os arquivos:
        - calculo.c: Contém duas funções para calcular o fractal de Mandelbrot, a partir dele será criada a biblioteca compartilhada (calcular.so);
        - calcular.so: Biblioteca compartilhada usada em python;
        - app_interface.py: Arquivo que gera uma interface e plota um gráfico com o fractal de Mandelbrot;
        - Makefile: Pode ser usado para automatizar a compilação e execução do trabalho.

## Bibliotecas necessárias
- numpy
- matplotlib

## Execução utilizando Makefile
    Abrir terminal linux ou com suporte para o comando 'make', e execupar a seguinte sequência de comandos:
        - make
        - make run

## Execução passo a passo sem utilizar Makefile
Linux: 
- Abrir terminal;
- Navegue até a pasta que contém os arquivos (AppFractal);
- Execute o comando : gcc -shared -o calculo.so -fPIC calculo.c (O comando completo gcc -shared -o calculo.so -fPIC calculo.c compila o arquivo calculo.c em uma biblioteca compartilhada chamada calculo.so, que pode ser usada por programas que precisam acessar as funções definidas em calculo.c.)
- Execute o arquivo python (app_interface.py): python app_interface.py



