palavras = ('milho', 'teia', 'parente', 'pelo')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra.upper()}',end=' ')