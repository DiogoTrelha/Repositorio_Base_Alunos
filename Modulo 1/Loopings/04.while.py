# crie um codigo que faça a conversao de  moeda do real para dolar e vice-versa

#etapas da resoluçao:
# 1)criar uma variavel chamada cotaçao
# 2)solcitar ao usuario a opçao de conversao desejada
# 3) apresentar o resultado da convesao de moeda 
# 4) perguntar se ele deseja continuar a conversao


letra = "s"
while letra == "s":
    cotacao = float(input("digite a cotaçao do dolar: "))
    print("-"*50)
    print(f"-"*15,"escolha a opçao","-"*18)
    print("-"*50)

    opcao =int(input("1 - converter dolar para real |2 - conversor real para dolar: "))

    if opcao == 1:
        valor = float(input("digite o valor em dolar a ser convertido para real U$: "))
        resultado = valor * cotacao
        print(f"o valor em reais e: {resultado}")
    elif opcao == 2:
         valor1 = float(input("digite o valor em real a ser convertido para dolar r$: "))
         resultado = valor1/ cotacao
         print(f"o valor em dolar e: {resultado}")
    else:
        print("digite uma opçao valida")
    letra = input("deseja continuar? (s/n): ").lower()
    

