"""
Considere a empresa de telefonia Tchau.Abaixo de 200 minutos, a empresa
cobra R$ 0,20 por minuto.Entre 200 e 400 minutos, o preço é R$ 0,18.Acima de 400
minutos o preço por  minutos é 0,15. Calcule sua conta de telefone.
"""
__version__ = "1.0.0"
print(__version__)


#Autor : João Victor Barreto
#Funcionalidade : Calculo de Conta de Telefone
#Data : 29/01/2019

minutos = int(input("Minutos: "))

conta_telefone = 0

if minutos < 200:
    conta_telefone = minutos * 0.2 # 0,20 R$
    print("Você vai pagar R$: ", round(conta_telefone,2))
if minutos >= 200 and minutos <= 400:
    conta_telefone = minutos * 0.18 # 0,18 R$
    print("Você vai pagar R$: ", round(conta_telefone,2))
if minutos > 400:
    conta_telefone = minutos * 0.15 # 0,15 R$
    print("Você vai pagar R$: ", round(conta_telefone,2))
    
