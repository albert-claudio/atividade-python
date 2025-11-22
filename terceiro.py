produtos = {
    "Alimentação": [12.50, 8.99, 15.30],
    "Limpeza": [5.20, 7.80],
    "Higiene": [10.00, 12.00, 9.50, 14.00]
}

#variveis para armazenar a maior media e a categoria
maior_media = 0
categoria_maior_media = ""

for categoria, precos in produtos.items():
    media = sum(precos) / len(precos)
#verificando se é a maior media
    if media > maior_media:
        maior_media = media
        categoria_maior_media = categoria

print(f"Categoria com maior média de preços(vencedora): {categoria_maior_media} - Média: {maior_media:.2f}")
