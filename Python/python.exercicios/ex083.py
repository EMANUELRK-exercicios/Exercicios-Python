expr =(str(input('Digite uma expressão: ')))
pilha = list()
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(expr) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão valida!')
else:
    print('Expressao Invalida!')


