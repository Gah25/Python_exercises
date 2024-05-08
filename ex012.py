preco = float(input('Qual é o preço do produto? R$ '))

porcentagem = 5 / 100
preco_real = preco * porcentagem
preco_com_desconto = preco - preco_real

print(f'O produto que custava R${preco}, na promoção com desconto de 5% vai custar {preco_com_desconto:.2f}')
