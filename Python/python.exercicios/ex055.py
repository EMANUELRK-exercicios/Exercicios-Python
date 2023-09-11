print('PESAGENS:')
maior = 0
menor = 0
for c in range(1, 5):
    print('=' * 20)
    nome = str(input('Digite o {}° nome:'.format(c)))
    peso = float(input('Digite seu peso: (KG)'))
    if c == 1:
        maior = peso
        menor = peso
        pesado = nome
        leve = nome
    else:
        if peso > maior:
            maior = peso
            pesado = nome
        if peso < menor:
            menor = peso
            leve = nome
print('=' * 20)
print('{} foi o MAIOR peso foi:({}KG)'.format(pesado, maior))
print('{} foi o MENOR peso:({}KG)'.format(leve, menor))





