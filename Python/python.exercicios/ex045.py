from random import choice
from time import sleep
print('--JOKENPO--')
print('Vamos jogaaar!!')
print('Player1 começa jogando.')
player1 = str(input('PEDRA / PAPEL / TESOURA: ')).upper().strip()
print('=' * 16)
print('Iniciando...')
print('=' * 16)
sleep(3)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
lista = ['PEDRA', 'PAPEL', 'TESOURA']
player2 = choice(lista)
print('=' * 16)
print('Player1: {}'.format(player1))
print('Player2: {}'.format(player2))
print('-=' * 8)
if player1 == player2:
    print('POUXA!! ninguem ganhou. Empataram.')
elif player1 == 'PEDRA' and player2 == 'TESOURA':
    print('PLAYER1 VENCEU! \nPedra amassa a tesoura.')
elif player1 == 'PEDRA' and player2 == 'PAPEL':
    print('PLAYER2 VENCEU! \nPapel embrulha a pedra.')
elif player1 == 'TESOURA' and player2 == 'PAPEL':
    print('PLAYER1 VENCEU! \nTesoura corta o papel.')
elif player1 == 'TESOURA' and player2 == 'PEDRA':
    print('PLAYER2 VENCEU! \nPedra amassa a tesoura.')
elif player1 == 'PAPEL' and player2 == 'PEDRA':
    print('PLAYER1 VENCEU! \nPapel embrulha a pedra.')
elif player1 == 'PAPEL' and player2 == 'TESOURA':
    print('PLAYER2 VENCEU! \nTesoura corta o papel.')
else:
    print('JOGADA INVALIDA!!!')
print('-=' * 8)

