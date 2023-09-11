print('==== Exercicio035 ====')
print('-x-' * 15)
print('Analisador de triangulo')
print('-x-' * 15)
lado1 = float(input('Digite o primeiro lado:  '))
lado2 = float(input('Digite o segundo lado: '))
lado3 = float(input('Digite o terceiro lado: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os segmentos PODEM FORMAR um triangulo!')
else:
    print('Os segmentos NÃO PODEM FORMAR um triangulo.')

