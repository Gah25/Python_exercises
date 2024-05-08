print("Olá, bem vindo ao banco GLB")
casa = float(input('Valor da casa: R$ '))
salario = float(input('Qual seria o seu salário: R$ '))
anos = int(input('Quantos anos de financiamento? '))

porcentagem = (30/100 * salario) + salario 
porcentagem_mensal = porcentagem - salario

prestacao = casa / (anos * 12)

if prestacao < porcentagem_mensal:
    print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${prestacao:.2f}')
    print('Empréstimo pode ser CONCEDIDO!')

elif prestacao == porcentagem_mensal:
    print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${prestacao:.2f}')
    print('Empréstimo pode ser CONCEDIDO!')

else:
    print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${prestacao:.2f}')
    print('Empréstimo NEGADO!')

