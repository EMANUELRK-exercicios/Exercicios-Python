from datetime import date
print('Maioridade:')
anoatual = date.today().year
maior = 0
menor = 0
for c in range(1, 3):
    print('-' * 20)
    nome = str(input('nome da {}° pessoa: '.format(c)))
    nasc = int(input('Ano nascimento: '))
    print('-' * 20)
    idade = anoatual - nasc
    if idade >= 21:
        maior = maior + 1
        print('{} é MAIOR de idade.'.format(nome))
        print('Idade: {}'.format(idade))
    else:
        menor = menor + 1
        print('{} é MENOR de idade.'.format(nome))
        print('Idade: {} anos.'.format(idade))
print('-' * 20)
print('Total de maiores de idade: {}'.format(maior))
print('Total de menor de idade: {}'.format(menor))

