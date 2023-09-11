n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
n4 = float(input('Quarta nota: '))
media = (n1 + n2 + n3 + n4) / 4
if media >= 7:
    print('\033[1;32mParabens!! voce foi aprovado com media {:.1f}\033[m'.format(media))
elif 7 > media >= 5:
    print('\033[1;33mCuidado!! voce entrou em RECUPERAÇÃO com media {:.1f}!\033[m'.format(media))
elif media < 5:
    print('\033[1;31mAtenção! Sua media foi {:.1f} voce está REPROVADO.\033[m'.format(media))