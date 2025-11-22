#recber numero do usuario
numero = (input("Digite um número inteiro: "))

#verificar se pode ser convertido para float
try:
    numero_float = float(numero)
    print(f"O número {numero} pode ser convertido para float: {numero_float}")
except ValueError:
    print(f"O número {numero} não pode ser convertido para float.")

