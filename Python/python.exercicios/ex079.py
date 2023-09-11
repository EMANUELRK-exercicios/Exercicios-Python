val = 0
valor = list()
while True:
    val = int(input('Digite um valor: '))
    if val not in valor:
        valor.append(val)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! não vou acidionar.')
    resp = str(input('Quer continuar?(S/N): ')).upper()[0]
    if resp in 'N':
        break
print('=' * 30)
print(f'Voce digitou os valores {sorted(valor)}')
