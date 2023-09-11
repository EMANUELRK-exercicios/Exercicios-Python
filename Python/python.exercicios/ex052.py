from time import sleep
print('NUMEROS PRIMOS:')
n = int(input('Digite um numero: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        tot += 1
        print('\033[1;31m{}\033[m'.format(c), end='  ')
        sleep(0.5)
    else:
        print('\033[m{}'.format(c), end='  ')
        sleep(0.5)
print('\nO numero {} foi divisiveis {} vezes.'.format(n, tot))
if tot == 2:
    print('Por tanto ele É PRIMO.')
else:
    print('Por tanto ele NÃO É PRIMO.')
print('FIM')
