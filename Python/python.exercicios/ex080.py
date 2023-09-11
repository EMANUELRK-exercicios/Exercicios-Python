lista = list()
for c in range(0, 5):
    v = int(input('Digite um valor: '))
    if c == 0 or v > lista[-1]:
        lista.append(v)
        print(f'O numero {v} foi adicionado na ultima posição')
    else:
        pos = 0
        while pos < len(lista):
            if v <= lista[pos]:
                lista.insert(pos, v)
                print(f'O numero {v} foi adicionado na {pos}° posição')
                break
            pos += 1
print(f'Os valores digitados foram {lista}')