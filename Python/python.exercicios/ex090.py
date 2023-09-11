dados = {}
dados['nome'] = str(input('Nome: '))
dados['media'] = float(input(f'Media de {dados["nome"]}: '))
if dados['media'] >= 7:
    dados['situação'] = 'APROVADO'
else:
    if dados['media'] < 7:
        dados['situação'] = 'REPROVADO'
for c, k in dados.items():
    print(f'{c} = {k}')

