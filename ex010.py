real = float(input('Quanto dinheiro você tem na carteira? R$'))

dolar = 4.86
conversor_dolar = real / dolar
print(f'Com R${real:.2f} você pode comprar US${conversor_dolar:.2f}')