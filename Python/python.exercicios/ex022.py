print('==== Exercicio022 ====')
nome = str(input('Digite seu nome completo: ')).strip()
print('Nome maiusculo: {} '.format(nome.upper()))
print('Nome minusculo: {}'.format(nome.lower()))
print('Total de letras no seu nome: {}'.format(len(nome)-nome.count(' ')))
nome = nome.split()
print('Qts str no primeiro nome: {}'.format(len(nome[0][0:])))






