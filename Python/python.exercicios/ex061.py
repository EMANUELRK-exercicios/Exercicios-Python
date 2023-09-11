from time import sleep
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
qnt = int(input('Digite quantos termos:'))
c = 0
print('Os 10 primeiros termos da PA: ')
while c <= qnt:
    sleep(0.5)
    print(p, end=' ')
    p = p + r
    c += 1

