## Verificador de planos de internet

# Criando a função
def recomendar_plano(consumo):
    if consumo <= 10:
        print("Plano recomendado:")
        print("Plano Essencial Fibra - 50Mbps")
    elif (consumo > 10) and (consumo <=20):
        print("Plano recomendado:")
        print("Plano Prata Fibra - 100Mbps")
    else:
        print("Plano recomendado:")
        print("Plano Premium Fibra - 300Mbps")

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input("Diga qual o seu consumo médio mensal de dados em GB\n"))

# Chama a função 
recomendar_plano(consumo)