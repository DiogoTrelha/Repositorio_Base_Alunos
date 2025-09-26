# criar um arquivo chamado mensagem.txt e escrever uma frase
# utilizando a with open() nao precisamos utilizar o close() pois o arquivo sera
# fechado ao final da execuçao

with open('mensagem.txt','w', encoding='utf-8') as arquivo:
    arquivo.write('Python facilita a vida!')
