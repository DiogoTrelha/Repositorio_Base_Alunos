# tipo de triangulo 
# crie um programa que receba tres lados de um triangulo
# verifique se os lados realmente podem formar um triangulo
# e determine os triangulos em:
# equilatero (todos os lados sao iguais)
# isosceles (dois lados iguais)
# escaleno(todos os lados diferentes)

a = int(input("digite o valor de lado a: ")) 
b = int(input("digite o valor de lado b: "))                           
c = int(input("digite o valor de lado c: "))

# verificar se os lados formam um triangulo
if a + b > c and a + c > b and b + c > a: # condiçao para formaçao do triangulo
    if a == b:
        if b == c:
            print(f"os lados do sao {a},{b},{c}:triangulo equilatero")
        else:
             print(f"os lados do sao {a},{b},{c}:treiangulo isosceles")
    else: # nao e possivel formar um triangulo
        if b == c or a == c:
           print(f"os lados do sao {a},{b},{c}:triangulo isosceles")
        else:
          print(f"os lados do sao {a},{b},{c}:triangulo escaleno")
else:
    print("os lados nao foram um triangulo valido")




