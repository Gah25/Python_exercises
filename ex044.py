print('=' * 10, "LOJAS GLB", '=' * 10)
produto = float(input('Qual é o preço das compras? '))

desconto_10 = produto - (10 / 100 * produto)
desconto_5 = produto - (5 / 100 * produto)
juros_20 = produto + (20 / 100 * produto)

print('''Formas de pagamento!
[ 1 ] À VISTA -> DINHEIRO / CHEQUE
[ 2 ] À VISTA CARTÃO
[ 3 ] PARCELADO EM 2X NO CARTÃO
[ 4 ] PARCELADO EM 3X OU MAIS NO CARTÃO
''')
opcao = int(input('Qual a forma de pagamento? '))

if opcao == 1:
    total = desconto_10
    print(f'O produto à vista no dinheiro ou cheque tem 10% de desconto e fica R${desconto_10}')
elif opcao == 2:
    total = desconto_5
    print(f'O produto à vista no cartão tem 5% de desconto e fica R${desconto_5}')
elif opcao == 3:
    total = produto
    parcela = total / 2
    print(f'A compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')
elif opcao == 4:
    total = juros_20
    total_parcelas = int(input('Quantas parcelas? '))
    parcela = total / total_parcelas
    print(f'Sua compra será parcelada em {total_parcelas}x de R${parcela:.2f} COM JUROS')
else:
    total = produto
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print(f'Sua compra de R${produto:.2f} vai custar R${total:.2f} no final.')
