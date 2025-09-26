num = int(input("digite um numero inteiro: "))
# 2) condicional para verificar se o numero e maior ou igual a zero
if num >=0:
    # condicional para checar se o numero e zero
    if num == 0:
    
        print("o numero digitado e zero") # informa que o numero e zero
    else:
        print(f"o numero {num} e positivo.")
else:
    print(f"o numero {num} e negativo.")