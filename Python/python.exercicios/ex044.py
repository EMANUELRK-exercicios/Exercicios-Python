valor = float(input('Qual o valor do produto:R$'))
print('O produto custa {}'.format(valor))
print('--Formas de pagamento-- ')
print('[ 1 ] Dinheiro / cheque. 10% de desconto.')
print('[ 2 ] Á vista no cartão. 5% de desconto.')
print('[ 3 ] Em até 2x no cartão. preço normal.')
print('[ 4 ] 3x ou mais no cartão. 20% de juros.')
escolha = int(input('Digite sua opção: '))
if escolha == 1:
    desc = (valor * 10) / 100
    print('Voce recebeu R${:.2f} de desconto e irá pagar apenas R${:.2f}.'.format(desc, valor - desc))
elif  escolha == 2:
    desc = (valor * 5) / 100
    print('Voce recebeu R${:.2f} de desconto no cartão e irá pagar apenas R${:.2f}.'.format(desc, valor - desc))
elif escolha == 3:
    print('Sua compra será parcelada em 2x de R${} sem nenhum desconto.'.format(valor / 2))
elif escolha == 4:
    juros = (valor * 20) / 100
    total = valor + juros
    parcela = int(input('Quantas parcelas? '))
    totparcel = total / parcela
    print('Sua compra será parcelada em {} vezes.'.format(parcela))
    print('Mas com juros de R${:.2f} tornando o valor total em R${:.2f} e pagando R${} por mes.'.format(juros, total, totparcel))
else:
    print('OPÇÃO INVALIDA DE PAGAMENTO! tente novamente.')