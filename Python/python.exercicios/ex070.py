nome = continuar = ''
preço = totvalor = mil = menor = 0
barato = ''
print('==' * 12)
print('LOJA DE ELETRONICOS')
print('==' * 12)
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço:R$ '))
    print('==' * 12)
    if totvalor == 0 or preço < menor:
        menor = preço
        barato = nome

    if preço > 1000:
        mil += 1
    totvalor += preço
    continuar = str(input('Quer continuar[S/N]: ').strip().upper()[0])
    while continuar not in 'SN':
        continuar = str(input('Quer continuar[S/N]: ').strip().upper()[0])
    if continuar in 'nN':
        break
print('FIM DAS COMPRAS!')
print(f'Total de gastos foi de R${totvalor:.2f}')
if mil != 0:
    print(f'{mil} Produtos custam mais de R$1000,00.')
else:
    print('Não foi vendido nenhum produto a cima de R$1000,00.')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')

