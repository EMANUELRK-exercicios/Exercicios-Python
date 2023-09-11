print('Calculando IMC')
peso = float(input('Digite qual seu peso(KG): '))
altura = float(input('Digite sua altura(M): '))
imc = peso / (altura ** 2)
print('IMC: {:.2f}'.format(imc))
if imc < 18.5:
    print('Voce está ABAIXO do peso.')
elif imc >= 18.5 and imc <= 25:
    print('Voce está no PESO IDEAL.')
elif imc > 25 and imc <= 30:
    print('Voce está com SOBREPESO. Obesidade grau 1')
elif imc > 30 and imc < 40:
    print('Voce está com OBESIDADE grau 2.')
elif imc >= 40:
    print('Voce está com OBESIDADE MORBIDA. grau 3.')