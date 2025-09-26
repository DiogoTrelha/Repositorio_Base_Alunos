# cire um codigo que receba 3 notas, calcule a media
# e informe se se o aluno esta aprovado, em recuperaçao
# ou reprovado

#OBS: aprovado >= 7
#recuperaçao media > 4
#reprovado < 4

#etapas
# 1) solicitar as notas do usuario
# 2)calcular a media
# 3) checar a condiçao do aluno
# 4) informar o resultado
n1 =float(input("digite a primeira nota: "))
n2 =float(input("digite a segunda nota: "))
n3 =float(input("digite a terceira nota: "))
media = (n1+n2+n3)/3
if media>=7:
    print(f"O aluno tem media{media:.2f} e esta aprovado.")
elif   5 <= media < 7 :
    print(f"O aluno tem media{media:.2f} e esta em recuperaçao.")
else:
    print(f"o aluno tem media{media:.2f} e esta reprovado.")