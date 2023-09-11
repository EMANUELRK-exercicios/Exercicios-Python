from time import sleep

opçao = 0

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite outro valor: '))
while opçao != 5:
    print('-' * 20)
    print('[1] para somar.')
    print('[2] para multiplicar.')
    print('[3] para maior.')
    print('[4] novos numeros.')
    print('[5] sair do programa.')
    print('-' * 20)
    opçao = int(input('Qual sua opção: '))
    print('-' * 20)
    if opçao == 1:
        print('A soma de {} + {} é igual a {}'.format(n1, n2, n1 + n2))
    elif opçao == 2:
        print('A multiplicação de {} * {} é igual a {}'.format(n1, n2, n1 * n2))
    elif opçao == 3:
        maior = 0
        if n1 > maior:
            maior = n1
        if n2 > maior:
            maior = n2
        print('Entre {} e {} o MAIOR é o {}'.format(n1, n2, maior))
        print('-' * 20)
    elif opçao == 4:
        print('Informe os numeros novamente: ')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite outro valor: '))
    elif opçao == 5:
        print('FINALIZANDO...')
    else:
        print('Opção INVALIDA! tente novamente')
    sleep(2)
print('Voce encerrou o PROGRAMA!!')