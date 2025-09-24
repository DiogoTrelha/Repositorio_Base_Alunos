# utilizamos o try/expept para apresentar uma exceçao
# de uma maneira mais amigavel ao usuario

try: # o codigo tenta executar o comando
    resultado = 10/0
except: # caso nao consiga, ele apresenta qual e o erro
    print('ocorreu um erro na operaçao. nao e possivel a divisao com dominador igual a zero')