pessoa = list()
grupo = list()
menor = maior = 0
while True:
    pessoa.append(str(input('NOME: ')))
    pessoa.append(int(input('PESO: ')))
    if len(grupo) == 0:
        maior = pessoa[1]
        menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    grupo.append(pessoa[:])
    pessoa.clear()
    r = str(input('Quer continuar?(S/N): ')).upper()[0]
    if r in 'N':
        break
print('=-' * 25)
print(f'Os dados foram {grupo}')
print(f'Ao todo temos {len(grupo)} pessoas cadastradas.')
print(f'O maior peso foi {maior}KG. Foi o peso de ', end='')
for p in grupo:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi {menor}KG. Foi o peso de ', end='')
for p in grupo:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
