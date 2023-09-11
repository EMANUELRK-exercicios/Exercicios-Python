ficha = list()
while True:
    nome = str(input('NOME: '))
    nota1 = float(input('NOTA1: '))
    nota2 = float(input('NOTA2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    r = str(input('Quer continuar?(S/N): ')).upper()[0]
    if r in 'N':
        break
print('-=' * 20)
print(f'{"N°":<4}{"NOME":<10}{"MEDIA":<8}')
print('-' * 25)
for i, l in enumerate(ficha):
    print(f'{i:<4}{l[0]:<10}{l[2]:<8.1f}')
print('-' * 25)
while True:
    opc = int(input('Mostrar nota de qual aluno?(999 imterrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha):
        print(f'As notas de {ficha[opc][0]} foram {ficha[opc][1]}')
    print('-' * 25)
print('-- <BOA NOITE> --')
