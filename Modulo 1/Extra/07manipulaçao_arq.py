# criar um arquivo nomes.txt

nomes = ['joao\n', 'maria\n','ana\n']

with open('nomes.txt','w', encoding='utf-8') as arquivo: # estamos criando o arquivo
    arquivo.writelines(nomes) # estamos pedindo para escrever