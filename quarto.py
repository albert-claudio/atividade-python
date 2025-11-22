A = [2, 3, 5]
B = [1, 4, 2]

#funcao implementando os dois vetores
def soma_vetores(vetor1, vetor2):
    if len(vetor1) != len(vetor2):
        raise ValueError("Os vetores devem ter o mesmo tamanho.")
    return [a + b for a, b in zip(vetor1, vetor2)]
#retorna o produto escalar
def produto_escalar(vetor1, vetor2):
    if len(vetor1) != len(vetor2):
        raise ValueError("Os vetores devem ter o mesmo tamanho.")
    return sum(a * b for a, b in zip(vetor1, vetor2))
soma = soma_vetores(A, B)
produto = produto_escalar(A, B)
print("Soma dos vetores:", soma)
print("Produto escalar dos vetores:", produto)