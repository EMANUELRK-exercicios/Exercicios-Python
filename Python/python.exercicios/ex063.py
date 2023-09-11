n = int(input('Digite um numero: '))
c = 2
f = 0
pr = 0
seg = 1
print('{} {}'.format(pr, seg), end=' ')
while c < n:
    f = pr + seg
    print('{}'.format(f), end=' ')
    pr = seg
    seg = f
    c += 1
print('FIMM!')
