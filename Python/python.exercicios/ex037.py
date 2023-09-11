n = int(input('Digite um numero qualquer: '))
print('O numero digitado foi {}'.format(n))
print('Voce pode ver esse numero em outros formados!')
print('1 - BINARIO')
print('2 - OCTAL')
print('3 - HEXADECIMAL')
print('4 - TODAS OPÇÕES')

escolha = int(input('Escolha uma das opções: '))
if escolha == 1:
    print('O numero digitado em Binario é: {}'.format(bin(n)[2:]))
elif escolha == 2:
    print('O numero digitado em Octal é: {}'.format(oct(n)[2:]))
elif escolha == 3:
    print('O numero digitado em Hexadecimal é: {}'.format(hex(n)[2:]))
elif escolha == 4:
    print('O numero digitado em:\nBinario: {}\nOctal: {}\nHexadecimal: {}'.format(bin(n)[2:], oct(n)[2:], hex(n)[2:]))
else:
    print('Opção invalida! Escolha entre as opçoes a cima.')
