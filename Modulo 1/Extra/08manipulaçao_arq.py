# contar quantas linhas tem no arquivo

with open('pessoa.txt','r', encoding='utf-8')as arquivo:
    linhas = arquivo.readlines() # aqui estamos lendo o arquivo e armazenando a leitura na variavel linhas
    print(f'Total linhas: ',len(linhas))# a funçao len() conta quantas linhas tem  no arquivo lido