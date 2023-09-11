c = 0
s = 0
n = 0
while n != 999:
    n = int(input('Digite um numero [999 encerra o programa!]: '))
    if n != 999:
        c += 1
        s += n
print(f'Foram adicionados {c} numeros')
print(f'A soma total entre eles é de {s}')
print('FIM')
