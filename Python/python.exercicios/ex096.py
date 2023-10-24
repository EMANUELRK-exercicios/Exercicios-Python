def titulo(msg):
    print()
    print(msg)
    print('-' * 22)


titulo(' Controle de Terrenos')


def area(a, b):
    t = a * b
    print(f'A área de um terreno {a} x {b} é de {t:.1f}m²')


print()
l = float(input('LARGURA(m): '))
c = float(input('COMPRIMENTO(m): '))
area(l, c)
