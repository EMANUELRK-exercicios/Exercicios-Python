t = 0
while True:
    c = 0
    print('-' * 30)
    t = int(input('Digite a tabuada desejada: '))
    if t < 0:
        break
    while c < 10:
        c += 1
        print(f'{t} x {c} = {t * c}')
print('Programa tabuada ENCERRADO.')
