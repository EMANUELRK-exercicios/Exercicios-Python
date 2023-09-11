from random import randint
menor = maior = 0
c = 0
num = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print('Os valores sorteados foram: ', end=' ')
for n in num:
    print(f'{n} ', end='')

print(f'\nMAIOR:{max(num)}')
print(f'MENOR:{min(num)}')


