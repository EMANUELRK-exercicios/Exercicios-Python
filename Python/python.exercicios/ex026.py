print('==== Exercicio026 ====')
nome = str(input('Digite um nome: ')).upper().strip()
print('Qnts vezes "A" aparece: {}x'.format(nome.upper().count('A')))
print('A primeira letra "A" aparece na {}° posição.'.format(nome.find('A')+1))
print('A ultima letra "A" aparece na {}° posição.'.format(nome.rfind('A')+1))



