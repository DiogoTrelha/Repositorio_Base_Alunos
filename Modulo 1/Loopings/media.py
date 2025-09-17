notas =[] # criei uma lista vazia que ira armazenar as notas recebidas

for i in range(4): # faz a pergunta 4 vezes
    nota = float(input(f"informe a nota da prova {i+1}: "))
    if nota > 0: # so aceita nota positivas
        notas.append(nota) # notas.append(nota) adiciona um elemento no final da lista
    else: # se a nota for negativa aprensenta o print
        print("valor invalido")
print(f"sua notas sao : {nota}") # linha opcional
media = sum(notas)/len(notas) # a funçao sun(notas) soma todas as notas da lista
# a funçao len(notas) informa o tamanho da lista nostas

if media >=7: # se a media for maior que 7
    print(f"suas notas doram {notas}, sua {media:.2f} e voce esta aprovado")
elif 5 <= media < 7: # se a media for de 5 a 6.99
    print(f"suas notas doram {notas}, sua {media:.2f} e voce esta recuperaçao")
else: # notas abaixo de 5, ou seja, de 4.99 para baixo
    print(f"suas notas doram {notas}, sua {media:.2f} e voce esta reprovado")
# {mdia:.2f} formata a media para o resultado ter apenas 2 casas decimais