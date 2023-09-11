resp = 'S'
s = m = c = maior = menor = 0
while resp == 'S':
    n = int(input('Digite um N°: '))
    s += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar?(S/N): ')).upper()
m = s / c
print('A media entre os valores digitados é de {:.2f}'.format(m))
print('O MAIOR numero digitado foi {}'.format(maior))
print('O MENOR numero digitado foi {}'.format(menor))
print('FIM!')
