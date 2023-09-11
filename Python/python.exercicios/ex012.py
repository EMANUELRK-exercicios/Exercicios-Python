print('==== Exercicio012 ====')
pr = float(input('Digite o preço do produto: R$'))
desc = (pr * 5 /100)
nov = pr - desc
print('Parabens voce recebeu 5%({:.2f}R$) de desconto.'.format(desc))
print('O total era R${} e agora ira pagar apenas R${:.2f}'.format(pr, nov))
