lista = []
ficha = {}
totidade = media = 0
while True:
    ficha['nome'] = str(input('Nome: '))
    while True:
        ficha['Sexo'] = str(input('SEXO:[M/F]')).upper()[0]
        if ficha['Sexo'] in 'MF':
            break
        print('ERROR! por favor digite apenas M ou F.')
    ficha['idade'] = int(input('IDADE: '))
    lista.append(ficha.copy())
    totidade += ficha['idade']
    while True:
        r = str(input('Quer continuar?(S/N): ')).upper()[0]
        if r in 'SN':
            break
        print('ERROR! digite apenas S ou N.')
    if r in 'N':
        break
print('-=' * 30)
media = totidade / len(lista)
print(f'A) O grupo tem {len(lista)} pessoas.')
print(f'B) A media de idade é de {media:.2f}')
print('C) As mulheres cadastradas foram', end='')
for p in lista:
    if p['Sexo'] == 'F':
        print(f', {p["nome"]}', end='')
print()
print('D) Pessoas que estão acima da media de idade: ')
for p in lista:
    if p['idade'] >= media:
        print('     ')
        for k,v in p.items():
            print(f'{k} = {v};', end=' ')
        print()
print('<< ENCERRADO >>')
