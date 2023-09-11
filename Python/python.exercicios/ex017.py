from math import hypot
print('==== Exercicio017 ====')
co = float(input('Qual é o cateto oposto? '))
ca = float(input('Qual é o cateto adjacente?'))
hi = hypot(co, ca)
print('A soma dos quadrados dos catetos é igual a hipotenusa {:.2f}'.format(hi))

