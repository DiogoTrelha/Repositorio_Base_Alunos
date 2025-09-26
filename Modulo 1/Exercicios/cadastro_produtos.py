# cadastrar produtos com relatorio
# crie um programa em python que permita cadastrar produtos
# salvar essas informaçoes em um arquivo chamado produtos.txt
# o programa deve permitir:
# 1)inserir o nome do produto e preço
# 2)gravar os produtos no arquivo (um por linha)
# 3)ler os dados do arquivo e gerar um relatorio com:
#- lista de produtos cadastrados
#- media dos preços
#- o produto mais caro e o mais barato

# Cria o arquivo com os produtos
with open('produtos.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('cafe, 36.00\n')
    arquivo.write('cha, 10.00\n')
    arquivo.write('suco, 18.50\n')
    arquivo.write('refrigerante, 17.50\n')
    arquivo.write('agua, 5.50\n')

# Lê os produtos e preços
produtos = []
with open('produtos.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        nome, preco = linha.strip().split(',')
        produtos.append((nome.strip(), float(preco)))

# Inicializa variáveis para cálculo
total = 0
mais_caro = produtos[0]
mais_barato = produtos[0]

for nome, preco in produtos:
    total += preco
    if preco > mais_caro[1]:
        mais_caro = (nome, preco)
    if preco < mais_barato[1]:
        mais_barato = (nome, preco)

media = total / len(produtos)

# Escreve o relatório
with open('relatorio_produtos.txt', 'w', encoding='utf-8') as relatorio:
    relatorio.write('RELATÓRIO DE PRODUTOS\n')
    relatorio.write('---------------------\n')
    relatorio.write(f'Preço médio: R$ {media:.2f}\n')
    relatorio.write(f'Produto mais caro: {mais_caro[0]} - R$ {mais_caro[1]:.2f}\n')
    relatorio.write(f'Produto mais barato: {mais_barato[0]} - R$ {mais_barato[1]:.2f}\n')