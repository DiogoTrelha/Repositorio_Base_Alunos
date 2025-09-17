# crie um programa que leia o peso de 5 pessoas.
# no final mostre qual foi o maior e o menor peso lido.


#etapas para resoluçao:
#1) crie uma lista vazia para receber os pesos
#2) crie um for para receber os pesos das 5 pessoas.
#3) adicione os pesos recebidos a lista
#4) utilize a funçao max() e min() ou ordene a lista e busque o primeiro e o ultimo elemento
#5) apresneta os resultados

pesos = []

for i in range(5):
    peso = float(input(f"informe seu peso em kg: "))
    pesos.append(peso)
print(f"A lista dos pesos em kg: ")

#maior_peso = max(pesos)
#menor_peso = min (pesos)
#print(f"o maior peso e {maior_peso} kg e o menor peso e {menor_peso} kg.")

pesos.sort()
menor = pesos[0]
maior = pesos [-1]
print(f"o maior peso e {maior} kg e o menor peso e {menor} kg.")


    
