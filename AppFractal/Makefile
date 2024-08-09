# Nome da biblioteca compartilhada
LIBRARY = calculo.so

# Nome do arquivo fonte da biblioteca
SRC = calculo.c

# Compilador e flags
CC = gcc
CFLAGS = -Wall -Wextra -fPIC
LDFLAGS = -shared

# Nome do script Python
PYTHON_SCRIPT = app_interface.py

# Regra para construir a biblioteca compartilhada
$(LIBRARY): $(SRC)
	$(CC) $(CFLAGS) $(LDFLAGS) -o $(LIBRARY) $(SRC)

# Regra para limpar arquivos temporários
clean:
	rm -f $(LIBRARY)

# Regra para executar o caso de estudo
run: $(LIBRARY)
	python3 $(PYTHON_SCRIPT)

# Regra padrão (executada por padrão)
all: $(LIBRARY)

.PHONY: clean run all