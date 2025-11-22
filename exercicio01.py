numero = [1,2,3,4,5,6,7,8,9,10]

def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
primos = [num for num in numero if eh_primo(num)]
nao_primos = [num for num in numero if not eh_primo(num)]

print("Números primos:", primos)
print("Números não primos:", nao_primos)