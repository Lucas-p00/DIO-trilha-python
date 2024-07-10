class Plano:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

    def verificar_saldo(self):
        return self.__saldo

    def custo_chamada(self, duracao):
        return 0.10 * duracao

    def deduzir_saldo(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            return True
        else:
            return False

class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.__nome = nome
        self.__numero = numero
        self.__plano = plano

    def fazer_chamada(self, destinatario, duracao):
        custo = self.__plano.custo_chamada(duracao)
        if self.__plano.deduzir_saldo(custo):
            saldo_restante = self.__plano.verificar_saldo()
            return f"Chamada para {destinatario} realizada com sucesso. Saldo restante: ${saldo_restante:.2f}"
        else:
            return "Saldo insuficiente para realizar a chamada."

    def __str__(self):
        return f"Usuário {self.__nome} criado com sucesso."

class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))

# Recebendo as informações do usuário:
nome = input("Digite o nome do usuário: ")
numero = input("Digite o número do telefone do usuário: ")
saldo_inicial = float(input("Digite o saldo inicial do usuário: "))

usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input("Digite o número do destinatário: ")
duracao = int(input("Digite a duração da chamada em minutos: "))

print(usuario_pre_pago.fazer_chamada(destinatario, duracao))
