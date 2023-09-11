listagem = ('Lapis', 1.75,
           'Borracha', 2.00,
           'Caderno',15.50,
           'Estojo', 8.65,
           'Transferidor', 4.20,
           'Compasso', 9.99,
           'Mochila', 120.75,
           'Canetas', 22.30,
           'Livro', 34.90)
print("=" * 40)
print(f'{"LISTA DE PREÇOS":^35}')
print("=" * 40)
for pos in range (0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30} R$', end=' ')
    else:
        print(f'{listagem[pos]:>5}')
print('=' * 40)
