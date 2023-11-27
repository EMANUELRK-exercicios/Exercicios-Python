def ficha(jog='<desconhedido>', gol=0):
    print(f'O jogador {jog} fez um total de {gol} gol(s) na temporada')


n = str(input('Nome do jogador: '))
g = str(input('Total de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)