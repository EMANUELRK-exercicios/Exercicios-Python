lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar?(S/N): ')).upper()[0]
    if resp in 'Nn':
        break
print('=-' * 30)
print(f'Voce digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista! nas posições ', end='')
else:
    print('Não foi encontrado o numero 5 na lista.')
for pos, l in enumerate(lista):
    if lista[pos] == 5:
        print(f'{pos}...', end='')

