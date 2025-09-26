# crie um codigo python que verifique se o ano e bissexto ou nao
ano = int(input("digite um ano: "))

if ano % 4 == 0:
    if ano % 100 != 0 or  ano % 400 == 0:
       print(f"o ano {ano} e bissexto")
    else:
       print(f"o ano {ano} nao e bissexto." )
else:
   print(f"o ano {ano} nao e bissexto")