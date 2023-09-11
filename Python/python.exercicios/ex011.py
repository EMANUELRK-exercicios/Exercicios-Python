print('==== Exercicio011 ====')
a = float(input('Qual é a Altura da parede? '))
l = float(input('Qual é a Largura da parede? '))
area = (a * l)
resp = area / 2
print('Uma parede de {} x {} tem uma area de {:.2f} metros quadrado.'.format(a, l, area))
print('Voce vai precisar de {:.2f} litros de tinta'.format(resp))
