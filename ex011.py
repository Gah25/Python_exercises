largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

area_total = largura * altura
lata_tinta = 2 # litros
qtd_tinta = area_total / lata_tinta

print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area_total}m²')
print(f'Para pintar essa parede, você precisará de {qtd_tinta}l de tinta')