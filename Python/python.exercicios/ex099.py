import time


def linha():
    print('=-' * 15)


def maior(*num):
    print('Analisando os valores passados...')
    cont = 0
    top = 0
    for c in num:
        if cont == 0:
            top = c
        else:
            if c > top:
                top = c
        print(f'{c}.', end=' ')
        time.sleep(0.4)
        cont += 1
    print(f'Foram encontrados {cont} valores ao todo.')
    print(f'O MAIOR valor foi {top}')


linha()
maior(5, 4, 3, 9, 2)
linha()
maior(4, 3, 10, 2)
linha()
maior(4, 6, 9, )
linha()
maior(5, 7)
linha()
maior(4)
