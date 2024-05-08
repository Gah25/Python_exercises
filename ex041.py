ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = 2023
ano = ano_atual - ano_nascimento

print(ano)
if ano < 10:
    print('MIRIM')
elif ano > 9 and ano < 15:
    print('INFANTIL')
elif ano > 14 and ano < 20:
    print('JUNIOR')
elif ano > 19 and ano < 21:
    print('SÊNIOR')
else:
    print('MASTER')