import time
from random import randint
print('==== Exercicio028 ====')
computador = randint(0, 5)
print('-=-' * 19)
print('Vou pensar em um numero entre 0 e 5. Tente advinhar...')
print('-=-' * 19)
jogador = int(input('Em que numero eu pensei? '))
print('PROCESSANDO...')
time.sleep(2)
if jogador == computador:
    print('Voce acertou!! era o {} mesmo.'.format(computador))
else:
    print('Voce errou! eu pensei no {}. Mais sorte na proxima.'.format(computador))
