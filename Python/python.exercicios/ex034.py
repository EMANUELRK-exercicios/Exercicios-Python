print('==== Exercicio034 ====')
sal = float(input('Digite seu salario: '))
nsal = 0
if sal > 1250.00:
    nsal = (sal * 10) / 100 + sal
    print('Seu novo salario é R${:.2f}'.format(nsal))
else:
    nsal = (sal * 15) / 100 + sal
    print('Seu novo salario é R${:.2f}'.format(nsal))