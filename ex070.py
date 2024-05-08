
# JEITO QUE EU FIZ

print('-' * 20)
print('LOJA SUPER BARATÃO')
print('-' * 20)

total_gasto = 0
maior_1000 = 0
produto_mais_barato = ''
preco_mais_barato = float('inf')




while True:
    produto = str(input('Nome do produto: '))
    preco = int(input('Preço: R$'))
    total_gasto = total_gasto + preco  
    
    if preco >= 1000:
        maior_1000 += 1

    if preco < preco_mais_barato:
        preco_mais_barato = preco
        produto_mais_barato = produto
        barato = produto

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

print(f'O total gasto na compra foi de R${total_gasto:.2f}')
print(f'Temos {maior_1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato é o(a) {produto_mais_barato} que custa R${preco_mais_barato:.2f}')


###########################################################################

"""
# JEITO PROFESSOR GUANABARA

total = total_mil = menor = contador = 0
barato = ''

while True:
    produto = str(input('Nome do produto: '))
    preço = int(input('Preço: R$'))
    total += preço
    contador += 1

    if preço > 1000:
        total_mil += 1

    if contador == 1 or preço < menor:
        menor = preço
        barato = produto

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {total_mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi o(a) {barato} que custa R${menor:.2f}')"""