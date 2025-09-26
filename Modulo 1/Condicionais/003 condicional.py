# criar um codigo python que indica se a temperatura esta agradavel ou nao 
#condiçoes:
# temperatura >= 30  informar que esta muito quente
# temperatura >= 20 informar que a temperatura esta agradavel
# temperatura >= 10 informar que esta frio

#etapas pra resoluçao:
#1) solicitar a temperatura para o usuario
#2) verificar a condicional
#3) imprimir a respsta segundo a temperatura

temperatura = float(input("digite a temperatura do dia: "))
if temperatura >= 30:
    print(f" a temperatura do dia e  {temperatura} c e o dia esta muito quente")
elif temperatura >= 20:
    print(f" a temperatura do dia e  {temperatura} c e o dia esta com a temperatura agradavel")
elif temperatura >= 10:
    print(f" a temperatura do dia e  {temperatura} c e o dia esta frio")
else:
    print(f"a temperatura do dia e {temperatura} c e o dia esta uma bosta")