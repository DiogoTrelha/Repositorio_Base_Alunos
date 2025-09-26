#2.Paridade e tamanho do numero
# crie um codigo que receba um numero inteiro e informe:
#- se e par ou impar
#- e , ao mesmo tempo , se e maior que 10 ou menor ou igual a 10
# utilize condicionais aninhadas para organizar as verificaçoes

num = int(input("digite um numero inteiro: "))
if num % 2 == 0:
    if num >=10:
        print(f"o {num} e maior que 10 e par")
    else:
        print(f"numero {num} e menor que 10 e par")
else:
    if num >=10:
        print(f"o numero {num} e impar e maior que 10")
    else:
        print(f"o numero {num} e impar menor que 10")

