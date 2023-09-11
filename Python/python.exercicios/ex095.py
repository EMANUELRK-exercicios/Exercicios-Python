jogador = dict()
gols = list()
time = list()
while True:
    print('--' * 30)
    jogador['nome'] = str(input('Nome do jogador: '))
    partida = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, partida):
        gols.append(int(input(f'Quantos gols na {c + 1}° partida: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    gols.clear()
    while True:
        r = str(input('Quer continuar?(S/N)')).upper()[0]
        if r in 'SN':
            break
        print('ERROR! digite apenas S ou N.')
    if r in 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<16}', end='')
print()
print('--' * 30)
for k,v in enumerate(time):
    print(f'{k:<4}', end='')
    for d in v.values():
        print(f'{str(d):<16}', end='')
    print()
while True:
    opc = int(input('Mostrar dados de qual jogador?(999 encerra)'))
    if opc == 999:
        break
    if opc > len(time):
        print(f'ERROR! não existe jogador com o codigo {opc}')
    else:
        print(f' == Levantamento do jogador {time[opc]["nome"]}:')
        for i, v in enumerate(time[opc]['gols']):
            print(f'    ==> Na {i + 1}° partida, ele fez {v} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')

