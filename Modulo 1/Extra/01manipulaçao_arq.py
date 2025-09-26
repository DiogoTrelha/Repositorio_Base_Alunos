# criar arquivos, recebendo informaçao do usuario

# Solicitaçao de entrada
nome = input('digite seu nome completo: ')
email = input('digite seu e-mail: ')

# criar arquivo
arquivo = open('pessoa.txt','a',encoding='utf-8') # estamos criando o arquivo e armazrnar na variavel arquivo o modo 'a' escreve sempre no final,
#encoding utf-8 e para utilizar o conjunto de caracteres que engloba a lingua portuguesa
arquivo.write(nome + '|' + email + '\n') # .write e para escrever e o  \n e para pular linha
arquivo.close()# .close e para fechar o arquivo