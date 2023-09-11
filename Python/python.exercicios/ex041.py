from datetime import date
print('\033[1;36m---Confederação de Natação---\033[m')
print('Vamos descobrir qual categoria voce se encaixa:')
nasc = int(input('Digite seu ano de nascimento? '))
idade = date.today().year - nasc
print('Idade: {}'.format(idade))
if idade > 25:
    print('Categoria: Master')
elif idade <= 9:
    print('Categoria: Mirim')
elif idade <= 14:
    print('Categoria: Infantil')
elif idade <= 19:
    print('Categoria: Junior')
elif idade <= 25:
    print('Categoria: Senior')
