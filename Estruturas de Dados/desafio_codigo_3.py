# Validando número de telefone

import re

def validate_numero_telefone(phone_number):
    pattern = r"^\(\d{2}\) 9\d{4}-\d{4}$"

    if re.match(pattern, phone_number):  
        return "Número de telefone válido."
    else:
        return "Número de telefone inválido." 
    
# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
phone_number = input("Insira o número de telefone no formato (XX) 9XXXX-XXXX: ")  

# Imprime o resultado:
result = validate_numero_telefone(phone_number)

print(result)