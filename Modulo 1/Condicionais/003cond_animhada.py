#3. classificaçao por idade 
#faça um programa que leia a idade de uma pessoa e classifique-a em:
#criança : menor que 12 
#adolescente: entre 12 e 17 anos
#adulto: maior ou igual a 18 anos
#utilize a estrutura de condicional aninhada

idade = int(input("digite sua idade"))
if idade >0:
    if idade >= 18:
        print(f"voce tem {idade} anos e e adulto")
    elif 12 <= idade <=17:
        print(f"voce tem {idade} e e adolescente")
    else:
        print(f"voce tem {idade} e e uma criança")
else:
    print("idade nao pode ser negativa, digite uma idade valida")
