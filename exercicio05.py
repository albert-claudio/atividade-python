#recber numero do usuario
numero = (input("Digite um número inteiro: "))

#verificar se pode ser convertido para float
try:
    numero_float = float(numero)
    print(f"O número {numero} pode ser convertido para float: {numero_float}")
 #verificando se é par ou impar se for inteiro
    if numero_float.is_integer():
        numero_int = int(numero_float)
        if numero_int % 2 == 0:
            print(f"O número {numero_int} é par.")
        else:
            print(f"O número {numero_int} é ímpar.")
except ValueError:
    print(f"O número {numero} não pode ser convertido para float.")
