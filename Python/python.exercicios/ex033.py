print('==== Exercicio033 ====')
n1 = int(input('Digite o 1° numero: '))
n2 = int(input('Digite o 2° numero: '))
n3 = int(input('Digite o 3° numero: '))
maior = n1
menor = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print('Maior: {}'.format(maior))
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print('Menor: {}'.format(menor))
