#importando a biblcioteca collections
from collections import Counter

#receber frase do usuario
frase = input("Digite uma frase com mais de 3 caracteres: ")

#ver qual é o terceiro caractere mais comum
contador = Counter(frase)
mais_comum = contador.most_common()
#quantas occorencias do terceiro mais comum
if len(mais_comum) >= 3:
    terceiro_mais_comum = mais_comum[2]
    print(f"O terceiro caractere mais comum é '{terceiro_mais_comum[0]}' com {terceiro_mais_comum[1]} ocorrências.")
else:
    print("A frase não possui pelo menos três caracteres.")