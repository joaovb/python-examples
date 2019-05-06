velocidade_carro = int(input("Digite a velocidade do carro: "))

if velocidade_carro > 110:
    print("Você foi multado!")
    multa = (velocidade_carro - 110) * 5
    print("Valor da Multa : ", multa, "R$")
else:
    print("Você não foi multado")
    
