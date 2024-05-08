distancia = int(input('Qual a distância da viagem em km: '))


if distancia <= 200:
    valor_passagem_por_km = 0.50
    valor_passagem = distancia * valor_passagem_por_km
    print(f'O valor da passagem é R${valor_passagem:.2f}')

else:
    valor_passagem_por_km_acima_de_200 = 0.45
    valor_passagem_1 = distancia * valor_passagem_por_km_acima_de_200
    print(f'O valor da passagem é R${valor_passagem_1:.2f}')
