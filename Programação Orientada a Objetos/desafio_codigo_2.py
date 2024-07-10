class PlanoTelefone:
    def __init__(self, nome, saldo):
        self.__nome = nome
        self.__saldo = saldo

    def verificar_saldo(self):
        if self.__saldo < 10:
            return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif self.__saldo >= 50:
            return "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

    def mensagem_personalizada(self):
        return f"Plano: {self.__nome}, Saldo: {self.__saldo}"

class UsuarioTelefone:
    def __init__(self, nome, plano):
        self.__nome = nome
        self.__plano = plano

    def verificar_saldo(self):
        saldo_mensagem = self.__plano.verificar_saldo()
        return saldo_mensagem

    def __str__(self):
        return f"Usuário {self.__nome} criado com sucesso."

# Recebendo as entradas do usuário (nome, plano, saldo):
nome_usuario = input("Digite o nome do usuário: ")
nome_plano = input("Digite o plano do usuário (Essencial, Prata, Premium): ")
saldo_inicial = float(input("Digite o saldo inicial do usuário: "))

plano_usuario = PlanoTelefone(nome_plano, saldo_inicial) 
usuario = UsuarioTelefone(nome_usuario, plano_usuario)  

mensagem_usuario = usuario.verificar_saldo()  
print(mensagem_usuario)
