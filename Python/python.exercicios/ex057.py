sexo = str(input('Qual o sexo da pessoa? [M/F]: ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos! Por favor, informe o sexo: ')).upper().strip()[0]
print('Obrigado pela informação!!')
print('sexo {} registrado com sucesso!'.format(sexo))



