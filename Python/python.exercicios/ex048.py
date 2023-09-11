print('SOMANDO NUMEROS IMPARES E DIVISIVEIS POR 3: ')
s = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        cont += 1
        s = s + c
print('A SOMA DE {} VALORES SOLICITADOS É: {}'.format(cont, s))







