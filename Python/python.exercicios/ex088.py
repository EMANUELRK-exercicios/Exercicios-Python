import time
from random import randint
lista = list()
print('=-' * 10)
print('      MEGA SENA       ')
print('=-' * 10)
qnt = int(input('Quantas jogadas voce quer sortear? '))
tot = 1
jogos = list()
while tot <= qnt:
    cont = 0
    while True:
        val = randint(1, 60)
        if val not in lista:
            lista.append(val)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('=-' * 3, f'Sorteando {qnt} Numeros', '=-' * 3)
for i, l in enumerate(jogos):
    print(f'JOGOS {i + 1}: {l}')
    time.sleep(0.5)
print('=-' * 5, '<BOA NOITE>', '=-' * 5)


