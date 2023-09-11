import datetime
print('\033[1;32m---ALISTAMENTO MILITAR---\033[m')
nasc = int(input('Em que ano voce nasceu? '))
anoatual = datetime.date.today().year
idade = anoatual - nasc
alistamento = nasc + 18
menoridade = alistamento - anoatual
if idade < 18:
    print('Voce só tem {} anos, não tem idade ainda para se alistar.'.format(idade))
    print('Isto vai acontecer em {} Faltam {} ano(s)'.format(alistamento, menoridade))
elif idade == 18:
    print('Voce tem {} anos e está na idade certa para se alistar.'.format(idade))
    print('Procure uma unidade do exercito mais proxima de voce.')
elif idade > 18:
    print('Voce tem {} anos, Era pra ter se alistado em {}.'.format(idade, alistamento))
    print('Espero que tenha se alistado, pois se passaram {} ano(s).'.format(anoatual - alistamento))
