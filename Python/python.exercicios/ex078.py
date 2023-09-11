valores = list()
maior = 0
menor = 0
for v in range(0, 5):
    valores.append(int(input(f'Digite o {v}° numero: ')))
    if v == 0:
        maior = valores[v]
        menor = valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]
print(f'Os numeros digitados foram {valores}')
print(f'O MAIOR numero foi {maior} na posição ', end='')
for pos, v in enumerate(valores):
    if valores[pos] == maior:
        print(f'{pos}...', end='')
print()
print(f'O MENOR numero foi {menor} na posição ', end='')
for pos, v in enumerate(valores):
    if valores[pos] == menor:
        print(f'{pos}...', end='')

