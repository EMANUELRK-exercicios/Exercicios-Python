print('PALINDROMO:')
frase = str(input('Digite uma frase:')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
## 2 modelos a ser feito. utilizando 'FOR' ou fatiamento.
'''inverso = junto[::-1]'''
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('\033[34mTemos um palindromo!!.\033[m')
else:
    print('\033[31mA frase digitada NÃO É UM PALINDROMO.\033[m')









