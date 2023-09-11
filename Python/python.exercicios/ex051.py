print('PROGRESSÃO ARITMETICA')
inic = int(input('Qual o primeiro termo? '))
r = int(input('Qual a razão? '))
decimo = inic + (10 - 1) * r
for c in range(inic, decimo + r, r):
       print('{}'.format(c), end='  ')
print('\nPRIMEIRO TERMO: {}'.format(inic))
print('RAZÃO: {}'.format(r))
print('FIM')
