letra = 's'

while letra == 's':
    n1 = float(input("digiteum numero: "))
    n2 = float(input("digite a porcentagem que deseja descobrir: "))

    porcentagem = (n1*n2)/100
    print(f"a porcentagem e igual a: {porcentagem}")
    letra = input("deseja continuar? (s/n)").strip().lower()