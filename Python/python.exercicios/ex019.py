import random
print('==== Exercicio019 ====')
print('Um professor quer apagar e irá sortear qual alunos vai apagar o quadro entre eles.')
aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.choice(lista)
print('O aluno escolhido foi {}'.format(sorteio))
