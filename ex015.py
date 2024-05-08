aluguel = int(input('Quantos dias alugados? '))
km_rodados = float(input('Quantos Km rodados? '))

dias = aluguel * 60
valor_km = km_rodados * 0.15
valor_total = dias + valor_km

print(f'O total a pagar é de R${valor_total:.2f}')