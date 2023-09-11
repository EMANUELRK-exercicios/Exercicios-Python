from math import sin, cos, tan,radians
print('==== Exercicio018 ====')
num = float(input('Digite um angulo qualquer: '))
sen = sin(radians(num))
print('O angulo de {} tem o SENO de {:.2f}'.format(num, sen))
cos = cos(radians(num))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(num, cos))
tan = tan(radians(num))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(num, tan))
