'''
Boas Vindas
Sistema sorteia um número
Sistema solicita o nome do jogador
Sistema solicita ao jogador seu palpite
Se errou, informar se para mais ou para menos, solicitar outro palpite e
informar quantas tentativas ainda restam
Se acertou, parabenizar e informar o número de tentativas utilizadas.
Número máximo de tentativas = 7
'''
import random

chute = 0
chances = 7
tentativas = 1
jogador = ''
# sistema sorteará um número entre 1 e 100
numero_secreto = int(random.randint(1, 100))

print('####################################')
print('Bem vindo ao jogo de adivinha')
print('Você terá sete chances para adivinhar')
print('#####################################')

# programa solicita o nome do jogador
jogador = input('Digite seu nome: ')
print('Chute um número entre 1 e 100')

while tentativas <= 7:
    chute = int(input('Digite um número: '))
    if chute < numero_secreto:
        print('Você errou. Seu número é menor que o sorteado,'
              ' tente novamente.)')
        print('Tentativa %d de %d' % (tentativas, chances))
    elif chute == numero_secreto:
        print('PARABÉNS!!!!', jogador)
        print('Você acertou com %d tentativas' % tentativas)
        tentativas = 7
    else:
        print('Você errou, Seu número é maior que o sorteado,'
              ' tente novamente')
        print('Tentativa %d de %d' % (tentativas, chances))

    if tentativas == 6:
        print('Última tentativa')
    elif tentativas == 7:
        print('### Fim de jogo ###')
        print('O número sorteado foi o', numero_secreto)
    tentativas = tentativas + 1
