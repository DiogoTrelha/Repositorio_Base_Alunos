# crie um codigo python que verifique se a senha digitada
#pelo usuario for "1234", exiba "Acesso permitido".

#etapas de resoluçao
#criar uma variavel e atribuir a ela uma senha
#atraves de um input solicitar a senha ao usuario
#atraves da condicional checar se a senha e igual a senha armazenada
#liberar ou nao o acesso ao usuario

senha = "dass"
senha2 = input("digite sua senha: ")
if senha2 == senha:
    print(f"ACESSO PERMETIDO")
else:
    print(f"acesso negado. tente novamento")
