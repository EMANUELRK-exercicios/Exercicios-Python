print('==== Exercicio031 ====')
dist = int(input('Qual a distancia percorrida em KM: '))
print('Voce está prestestes a iniciar uma viagem de {}KM'.format(dist))
if dist <= 200:
    preço = (dist * 0.50)
    print('É considerada uma viagem curta.')
else:
    preço = (dist * 0.45)
    print('É considerada uma viagem longa.')
print('Voce irá pagar R${:.2f} na passagem'.format(preço))




