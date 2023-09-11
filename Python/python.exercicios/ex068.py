from random import randint
from time import sleep
c = s = 0
escolha = resp = ''
player = 0
while True:
    computador = randint(0, 3)
    print('==' * 12)
    print('Vamos jogar PAR ou IMPAR ')
    print('==' * 12)
    player = int(input('Escolha um numero (0 á 3): '))
    s = player + computador
    escolha = str(input('Par ou Impar[P/I]: ')).upper().strip()[0]

    while escolha not in 'PI':
        escolha = str(input('Par ou Impar[P/I]: ')).upper().strip()[0]
    print('==' * 12)
    if s % 2 == 0:
        print(f'PLAYER: {player}')
        sleep(1)
        print(f'COMPUTADOR: {computador}')
        sleep(1)
        print('RESULTADO: PAR')
        sleep(1)
        resp = 'P'
    else:
        print(f'PLAYER: {player}')
        sleep(1)
        print(f'COMPUTADOR: {computador}')
        sleep(1)
        print('RESULTADO: IMPAR')
        sleep(1)
        resp = 'I'
    print('==' * 12)
    if escolha == resp:
        c += 1
        print('Voce VENCEU!')
        sleep(1)
        print('Vamos jogar Novamente...')
        sleep(5)
    else:
        print('Voce PERDEU!')
        break
print(f'GAME OVER!! Voce venceu {c} vezes.')

