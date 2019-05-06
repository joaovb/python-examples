"""
Faça um programa que solicite um valor em reais, caso o valor for menor que
50,00, não terá desconto. entre 50,01 R$ e 89,00 R$ conceder desconto de 11.8%,
caso o valor seja entre 89,01 e 120,09 o desconto será de 18.9%,
acima de 120,09 o desconto será de 23.87%.

Autor : João Victor Barreto
Domínio : br.com.indra
Departamento : DevOps
"""

valor = float(input("Informe o valor R$: "))

if valor < 50:
    desconto = 0
    print("Você não ganhou desconto")
elif valor <= 89.01:
    desconto = 0.118
elif valor <= 120.09:
    desconto = 0.189
else:
    desconto = 0.2387
print("Você ganhou de desconto R$: ", (valor * desconto))
print("Porcentagem de desconto :", (desconto * 100), "%")

