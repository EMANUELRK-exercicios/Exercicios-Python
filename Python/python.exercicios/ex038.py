from time import sleep
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
print('\033[1;35mComparando numeros...\033[m')
sleep(3)
if n1 > n2:
    print('O primeiro numero ({}) digitado é o maior.'.format(n1))
elif n2 > n1:
    print('O segundo numero ({}) digitado é o maior.'.format(n2))
else:
    print('Não existe valor maior. Os dois são iguais.')