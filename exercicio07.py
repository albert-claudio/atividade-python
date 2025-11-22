livros = [
{"titulo": "A", "ano": 2020, "preco": 45},
{"titulo": "B", "ano": 2024, "preco": 80},
{"titulo": "C", "ano": 2020, "preco": 50},
{"titulo": "D", "ano": 2022, "preco": 40}
]

#usuario pesquisar o livro por título
titulo_pesquisa = input("Digite o título do livro que deseja pesquisar: ")
livro_encontrado = next((livro for livro in livros if livro["titulo"].lower() == titulo_pesquisa.lower()), None)
if livro_encontrado:

#filtrar livros por ano em ordem cronológica
    ano_pesquisa = livro_encontrado["ano"]
    livros_filtrados = [livro for livro in livros if livro["ano"] == ano_pesquisa]
    livros_ordenados = sorted(livros_filtrados, key=lambda x: x["preco"])
    print(f"Livros do ano {ano_pesquisa} em ordem de preço:")
    for livro in livros_ordenados:
        print(f"Título: {livro['titulo']}, Preço: {livro['preco']}")
else:
    print("Livro não encontrado.")
#fazer preço médio dos livros daquele ano
if livros_ordenados:
    preco_medio = sum(livro["preco"] for livro in livros_ordenados) / len(livros_ordenados)
    print(f"Preço médio dos livros do ano {ano_pesquisa}: {preco_medio:.2f}")
else:
    print("Nenhum livro encontrado para calcular o preço médio.")
