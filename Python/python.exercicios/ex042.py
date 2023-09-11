print('Descobrindo se os segmentos podem ser triangulos..')
l1 = float(input('Digite o primeiro lado: '))
l2 = float(input('Digite o segundo lado: '))
l3 = float(input('Digite o terceiro lado: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos PODEM formar um triangulo!')
    if l1 == l2 == l3:
        print('Isto é um triangulo EQUILÁTERO!!')
    if l1 != l2 != l3 != l1:
        print('Isto é um triangulo ESCALENO!!')
    else:
        print('Isto é um triangulo ISÓSCELES!!')
else:
    print('Os segmentos NÃO PODEM formar um triangulo!')
