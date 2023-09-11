numero = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
tot = len(numero)
while True:
    escolha = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= escolha <= 20:
        break
    print('Teste novamento.', end=' ')
print(f'Voce digitou o numero {numero[escolha]}')
