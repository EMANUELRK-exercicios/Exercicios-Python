print('==== Exercicio029 ====')
vel = float(input('Qual a velocidade em KM/H? '))
multa = ((vel - 80) * 7)
if vel > 80:
    print('MULTADO! voce está acima do limite de velocidade.')
    print('Voce irá pagar {:.2f}R$ de multa'.format(multa))
else:
    print('Voce está dentro do limite de velocidade.')

