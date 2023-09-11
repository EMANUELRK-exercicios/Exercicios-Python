soma_idade = 0
maior = 0
menor = 0
totF = 0
velho = ""
for c in range(1, 4):
    print('=' * 20)
    nome = str(input('Digite o {}° nome:'.format(c))).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo(M/F): ')).upper().strip()
    soma_idade += idade
    if c == 1:
        maior = idade
        menor = idade
    else:
        if idade > maior and sexo == "M":
            velho = nome
            maior = idade
    if idade < 20 and sexo == "F":
            totF += 1

media_idade = soma_idade / 3
print('A media de idade do grupo é : {:.2f}'.format(media_idade))
if velho != "":
    print('{} é o homem mais velho com {} anos.'.format(velho, maior))
else:
    print('Não há homens no grupo.')
if totF > 0:
    print('Existem {} mulheres com menos de 20 anos.'.format(totF))
else:
    print('Não há mulheres com menos de 20 anos.')

