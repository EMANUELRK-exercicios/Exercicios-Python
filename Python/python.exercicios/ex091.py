from time import sleep
from random import randint
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
rank= list()
print('Valores sorteados:')
sleep(0.5)
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(0.5)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('=-' * 20)
print('     == Ranking dos jogadores ==')
for i, v in enumerate(rank):
    print(f'   {i + 1}° lugar: {v[0]} com {v[1]} pontos.')
