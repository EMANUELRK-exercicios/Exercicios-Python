p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
total = 0
continuar = 10
print('-' * 20)
while continuar != 0:
    total += continuar
    while c <= total:
        print(p, end=' ')
        p = p + r
        c += 1
    continuar = int(input('\nQuer mostrar mais quantos termos? '))
    print('-' * 20)
print('FIM!!')
print('Total de {} termos exibidos:'.format(total))



