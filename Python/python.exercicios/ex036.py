from time import sleep
print('\033[1;33m=/=/= Banco do Brasil =/=/=\033[m')
print('Bom dia!! vi que voce tem interesse em pegar um emprestimo para comprar uma casa.')
print('Estou aqui para ajudar!')
valor = float(input('Me informe o valor total da casa:R$'))
sal = float(input('Me informe o seu salario atual:R$'))
ano = int(input('Em Quantos anos deseja pagar? '))
parcela = ano * 12
valparcela = valor / parcela
porcsal = (sal * 30) / 100
print('A casa custando R${:.2f} e parcelada em {} vezes, ficará R${:.2f} por mes.'.format(valor, parcela, valparcela))
print('\033[35mPROCESSANDO...')
sleep(5)
if valparcela <= porcsal:
    print('\033[1;32mParabens!! seu emprestimo de R${:.2f} e parcelado em {} vezes de R${:.2f} por mes foi autorizado.\nVamos estar liberando o dinheiro nos proximos dias.'.format(valor, parcela, valparcela))
else:
    print('\033[1;31mEmprestimo negado!')
    print('Infelizmente o valor por mes da parcela de R${:.2f}, ultrapassa 30% do seu salario que é de R${:.2f}'.format(valparcela, porcsal))
