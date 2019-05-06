'''
Criar uma função que me lembre a parar de estudar e fazer uma pausa a cada 2h
Trabalho inicia de 8h as 12h
'''

import webbrowser
import time

intervalos = 2
contador = 0
print('O programa de controle de descanso foi ativado')

while contador < intervalos:
    time.sleep(10)
    webbrowser.open_new('https://google.com.br')
    contador = contador + 1
