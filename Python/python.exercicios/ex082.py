lista = list()
par = list()
impar = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar?(S/N): ')).upper()[0]
    if r in 'N':
        break
print('=-' * 10)
print(f'A lista completa é {lista}')
for pos in range(0, len(lista)):
    if lista[pos] % 2 == 0:
        par.append(lista[pos])
    else:
        impar.append(lista[pos])
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')

