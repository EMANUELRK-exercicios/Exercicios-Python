jogador = {}
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = []
for c in range(0, partidas):
    gols.append(int(input(f'Gols na {c + 1}° partida: ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('=-' * 30)
print(f'{jogador}')
print('=-' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('=-' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    ==> Na {i + 1}° partida, ele fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')