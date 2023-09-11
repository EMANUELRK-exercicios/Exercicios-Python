print('==== Exercicio013 ====')
sal = float(input('Digite o seu salario: R$'))
nsal = float(sal * 15/ 100) + sal
print('Parabens! voce recebeu 15% de aumento no seu salario.')
print('Voce recebia R${} e agora vai passar a receber R${:.2f}'.format(sal, nsal))
