print('SOMANDO NUMEROS PARES.')
s = 0
cont = 0
for c in range(1, 6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        s += n
        cont += 1
print('A SOMA DOS PARES É {} COM {} NUMEROS DIGITADOS'.format(s, cont))
print('FIM')
