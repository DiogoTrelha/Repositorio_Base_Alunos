# crie um programa  que some todos os numeros impares
# que sao multiplos de 3 e 1 a 30 e apresente o resultado.

#Etapas para resoluçao
# 1) criar um for de  para captar os numeros impares
# 2) criar uma condicional para checar se o numero e multiplo de 3
# 3)somar os numeros que atende a condicional
# 4) apresentar os resultados

multiplos_tres = 0 # variavel que ira receber os numeros impares e multiplos de 3

for i in range(1,31,2): # contagem dos numeros impares
    if i % 3 == 0: #checagem se os numeros sao multiplos
        print(i, end=",") # apresentaçao dos nuemeros que atendam os requisitos(na mesma linha, separados por uma virgula,)
        multiplo_tres += i
print() # pular uma linha
print(f"A soma dos numeros impares multiplos de 3 neste intervalo e {multiplo_tres}.")