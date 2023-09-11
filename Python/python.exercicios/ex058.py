from time import sleep
from random import randint
computador = randint(0, 10)
jogador = 0
palpite = 0
acertou = False
print('\033[31mJogo de Adivinhação de 0 a 10.\033[m')
print('Computador irá escolher:')
print('PENSANDO...')
sleep(2)
while not acertou:
    jogador = int(input('Escolha o seu numero: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if computador > jogador:
            print('ERROU! tente um numero MAIOR')
        elif computador < jogador:
            print('ERROU! tente um numero MENOR')

print('Voce acertou!!!')
print('Era o numero {} mesmo.'.format(computador))
print('Voce precisou de {} tentativas.'.format(palpite))