matriz = [0, 0, 0], [0, 0, 0], [0, 0, 0]
totpar = Scoluna = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
        if matriz[l][c] % 2 == 0:
            totpar += matriz[l][c]
for l in range(0, 3):
    Scoluna += matriz[l][2]
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    else:
        if matriz[1][c] > maior:
            maior = matriz[1][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('=-' * 15)
print(f'Soma total PARES: {totpar}')
print(f'Soma dos valores da TERCEIRA coluna: {Scoluna}')
print(f'O maior numero da SEGUNDA linha: {maior}')

