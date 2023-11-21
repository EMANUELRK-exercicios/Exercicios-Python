import datetime
atual = datetime.date.today().year
def voto(ano):
    if idade >= 18:
        return 'VOTO OBRIGATORIO'
    if idade < 18 and idade >= 16:
        return 'VOTO OPCIONAL'
    else:
        return 'NÃO VOTA'


print()
anonasc = int(input('Em que ano voce nasceu: '))
idade = atual - anonasc
resp = voto(idade)
print(f'com {idade} anos: {resp}')


