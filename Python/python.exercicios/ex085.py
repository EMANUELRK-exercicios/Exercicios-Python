dado = 0
lista = [[], []]
for c in range(1, 8):
    dado = int(input(f'Digite o {c}° Valor:'))
    if dado % 2 == 0:
        lista[0].append(dado)
    else:
        if dado % 2 == 1:
            lista[1].append(dado)
print(f'Lista completa: {lista}')
print('=-' * 20)
print(f'PARES: {sorted(lista[0])}')
print(f'IMPARES:{sorted(lista[1])}')