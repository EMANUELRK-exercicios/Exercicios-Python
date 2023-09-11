tabela = ('botafogo', 'flamengo', 'fluminense', 'palmeiras', 'bragantino', 'gremio', 'atletico-pr', 'cuiabá', 'são paulo', 'atletico-mg', 'cruzeiro', 'internacional', 'fortaleza', 'corinthias', 'goias', 'bahia', 'santos', 'coritiba', 'vasco', 'america mg')
tot = len(tabela)
print('Tabela do Brasileirão: ')
for t in range (0, len(tabela)):
    print(f'{1 + t} - {tabela[t]}')
print('=-' * 10)
print('Os 5 primeiros colocados: ')
#for t in range (0, 5):
#    print(f'{1 + t} - {tabela[t]}')
print(f'{tabela[0:5]}')
print('=-' * 10)
print('Os 4 ultimos são: ')
print(f'{tabela[-4:]}')
print('=-' * 10)
print('Times em ordem alfabetica: ')
print(f'{sorted(tabela)}')
print('=-' * 10)
print('O BAHIA está na {}° posição'.format(tabela.index('bahia') + 1))



