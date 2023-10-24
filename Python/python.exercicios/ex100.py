from random import randint
num = list()


def sorteia():
    for c in range(0, 5):
        val = randint(0, 10)
        num.append(val)
    print(f'Sorteando {c + 1} valores da lista: {num} PRONTO!!')


def sorteiapar():
    totpar = 0
    for c in num:
        if c % 2 == 0:
            totpar += c
    print(f'Somando os valores pares da lista: {num}, temos {totpar}')


sorteia()
print()
sorteiapar()
