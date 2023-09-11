from datetime import date
ficha = {}
anoatual = date.today().year
ficha['nome'] = str(input('Nome: '))
ficha['idade'] = int(input('Ano nascimento: '))
ficha['idade'] = anoatual - ficha['idade']
ctps = int(input('Carteira de trabalho(0 não tem): '))
ficha['ctps'] = ctps
if ctps != 0:
    ficha['contratação'] = int(input('Ano de contratação: '))
    ficha['salario'] = float(input('Salario: R$ '))
    ficha['aposentadoria'] = (ficha['contratação'] - (anoatual - ficha['idade'])) + 35
print('=-' * 30)
for k, v in ficha.items():
    print(f'{k} tem o valor {v}')

