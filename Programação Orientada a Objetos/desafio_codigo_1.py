# ----- Desafio 1: Criando uma Classe de Usuário ----- #

import re

class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        # Encapsulando os atributos
        self.__nome = nome
        self.__numero = numero
        self.__plano = plano

    # Método especial __str__ para representar o objeto como string
    def __str__(self):
        return f"Usuário {self.__nome} criado com sucesso."

    # Métodos getter para acessar os atributos encapsulados
    def get_nome(self):
        return self.__nome

    def get_numero(self):
        return self.__numero

    def get_plano(self):
        return self.__plano

    # Métodos setter para modificar os atributos encapsulados, se necessário
    def set_nome(self, nome):
        self.__nome = nome

    def set_numero(self, numero):
        self.__numero = numero

    def set_plano(self, plano):
        self.__plano = plano

# Função para validar o número de telefone
def validar_numero(numero):
    pattern = r"^\(\d{2}\) 9\d{4}-\d{4}$"
    return re.match(pattern, numero)

# Entrada de dados
nome = input("Digite o nome do usuário: ")

# Validando o número de telefone
while True:
    numero = input("Digite o número de telefone do usuário (no formato (XX) 9XXXX-XXXX): ")
    if validar_numero(numero):
        break
    else:
        print("Número de telefone inválido. Por favor, insira no formato (XX) 9XXXX-XXXX.")

plano = input("Digite o plano do usuário (Essencial Fibra, Prata Fibra, Premium Fibra): ")

usuario = UsuarioTelefone(nome, numero, plano)
print(usuario)
