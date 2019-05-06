"""
Considere a empresa de telefonia Tchau.Abaixo de 200 minutos, a empresa
cobra R$ 0,20 por minuto.Entre 200 e 400 minutos, o preço é R$ 0,18.Acima de 400
minutos o preço por  minutos é 0,15. Calcule sua conta de telefone.
Caso seja maior que 800 minutos, a tarifa é 0,08 R$
"""

#Autor : João Victor Barreto
#Funcionalidade : Calculo de Conta de Telefone
#Data : 29/01/2019

minutos = int(input("Minutos utilizados: "))
if minutos < 200:
    preco  = 0.20
else:
    if minutos <= 400:
        preco = 0.18
    if minutos >= 400 and minutos <= 800:
        preco = 0.15
    else:
        preco = 0.08
print("Conta telefônica: R$%6.2f" % (minutos * preco))

    
