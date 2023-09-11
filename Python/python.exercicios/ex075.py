num = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')), int(input('Digite mais um valor: ')), int(input('Digite um ultimo valor: ')))
print(f'Voce digitou os valores {num}')
print(f'O numero 9 apareceu {num.count(9)} vez')
if 3 in num:
    print(f'O numero 3 está na {num.index(3) + 1}° posição')
else:
    print('O valor 3 não apareceu na tupla')
print('PARES: ', end='')
for n in num:
    if n % 2 == 0:
        print(f'{n} ', end='')


