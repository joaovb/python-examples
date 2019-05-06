"""
Considere a empresa de telefonia Tchau.Abaixo de 200 minutos, a empresa
cobra R$ 0,20 por minuto.Entre 200 e 400 minutos, o preço é R$ 0,18.Acima de 400
minutos o preço por  minutos é 0,15. Calcule sua conta de telefone.
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
    else:
        preco = 0.15
print("Conta telefônica: R$%6.2f" % (minutos * preco))

    
