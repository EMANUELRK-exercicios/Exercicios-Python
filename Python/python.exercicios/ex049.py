tabu = int(input('Escolha a tabuada desejada: '))
print('TABUADA DO {} :'.format(tabu))
print('=-' * 6)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(tabu, c, tabu * c))
print('=-' * 6)