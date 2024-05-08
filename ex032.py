from datetime import date

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
ano_bissexto = ano % 4 == 0 and ano % 100 or ano % 400 == 0

if ano == 0:
    ano = date.today().year

if ano_bissexto:
    print(f'{ano} é um ano BISSEXTO')

else:
    print(f'{ano} não é um ano BISSEXTO')