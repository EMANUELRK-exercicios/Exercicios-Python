from time import sleep
def linha():
    print('=-' * 18)
def contador(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p = p * (-1)
    if i < f:
        for cont in range(i, f + 1, p):
            print(f'{cont}.', end=' ')
            sleep(0.2)
        print('FIM!')
    if i > f:
        for cont in range(i, f - 1, - p):
            print(f'{cont}.', end=' ')
            sleep(0.2)
        print('FIM!')
linha()
print('Contagem de 1 até 10 de 1 em 1')
contador(1, 10, 1)
linha()
print('Contagem de 0 até 10 de 2 em 2')
contador(10, 0, 2)
linha()
print('Contagem personalizada:')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
linha()