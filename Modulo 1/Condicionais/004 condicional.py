# crie um codigo em python que peça um numero ao usuario
# e exiba "numero par" se ele for divisivel por 2.

#etapas de resoluçao:

#1) solicitar um numero ao usuario
#2) verificar se o numero e par ou impar
#3) informar se o numero e par ou impar

numero = float(input("digite seu numero: "))
if numero % 2 == 0:
    print(f"O numero {numero} e o par.")
else:
    print(f"O numero {numero} e o impar.")