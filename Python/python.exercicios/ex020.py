from random import shuffle
print('==== Exercicio020 ====')
print('O professor vai sortear a ordem de apresentação dos trabalhos: ')
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação será')
print(lista)