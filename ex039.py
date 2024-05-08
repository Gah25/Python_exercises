from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}')

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento') 
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos.')  
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}')

"""
####JEITO QUE EU FIZ####

ano_nascimento = int(input('Digite o ano de seu nascimento: '))
idade = 2023 - ano_nascimento
idade_alistamento = 18


if idade > idade_alistamento:
    print(f'Fazem {idade - idade_alistamento} anos que passou do prazo para se alistar ao serviço militar')

elif idade < idade_alistamento:
    print(f'Daqui {idade_alistamento - idade} anos você terá que se alistar')

else:
    print('Você tem 18 anos, aliste-se IMEDIATAMENTE')
"""