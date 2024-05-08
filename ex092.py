from datetime import datetime
dados = {}

dados['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
dados['Idade'] = datetime.now().year - nascimento
dados['Carteira de Trabalho'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['Carteira de Trabalho'] != 0:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35) - datetime.now().year)
print('=-' * 30)

for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')