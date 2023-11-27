def fatorial(f, show=False):
    
    n = 1
    for c in range(f, 0, -1):
        if show:
            print(f'{c}', end=' ')
            if c > 1:
                print('x ', end='')
            else:
                print('= ', end='')
        n *= c
    return n


print(fatorial(5, show=True))
