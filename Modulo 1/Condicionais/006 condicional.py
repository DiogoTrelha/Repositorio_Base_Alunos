# Crie um codigo python que peça o valor da conta. se for maior que r$100,00
#adicione uma gorjeta de 10% e exiba o total a pagar
#caso contrario, adicione uma gorjeta de 5%.

#etapas para resoluçao
#1) solicitar o valor da conta para o usuario
#2) se a conta for maior que 100 adicionar 10% de gorjeta e apresentar o total a pagar
#3) se a conta for que 100 adicionar 5% de gorjeta e apresentar o total a pagar

valor_da_conta = float(input("valor da conta: "))
if valor_da_conta >=100:
    valor_final = valor_da_conta + (valor_da_conta *0.1)
else:
    valor_final = valor_da_conta + (valor_da_conta *0.05)
    print(valor_final)