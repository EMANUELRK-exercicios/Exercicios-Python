idade = cont = masc = femi = 0
sexo = ''
continuar = ''
while True:
    print('--' * 12)
    print('CADASTRE UMA PESSOA: ')
    print('--' * 12)
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO[M/F]: ').strip().upper()[0])
    while sexo not in 'MF':
        sexo = str(input('SEXO[M/F]: ').strip().upper()[0])
    print('==' * 12)
    if idade >= 18:
        cont += 1
    if sexo in 'M':
        masc += 1
    if idade < 20 and sexo in 'F':
        femi += 1
    continuar = str(input('Quer continuar [S/N]: ').strip().upper()[0])
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]: ').strip().upper()[0])
    if continuar in 'N':
        break
print('--' * 12)
print('FIM DO PROGRAMA!')
print('--' * 12)
if cont == 0:
    print('Não temos pessoas MAIORES de idade cadastradas..')
else:
    print(f'Ao todo temos {cont} pessoa(s) MAIORES de 18 anos cadastradas..')
if masc != 0:
    print(f'Ao todo temos {masc} homens cadastrados.')
else:
    print('Não temos Homens cadastrados.')
if femi != 0:
    print(f'Ao todo temos {femi} mulheres com menos de 20 anos cadastradas.')
else:
    print('Não temos mulheres com menos de 20 anos cadastradas.')
