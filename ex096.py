def area():
    print('Controle de Terrenos')
    print('-' * 20)
    largura = float(input('LARGURA (m): '))
    comprimento = float(input('COMPRIMENTO (m): '))
    soma = largura * comprimento
    print(f'A área de um terreno {largura:.1f}x{comprimento:.1f} é de {soma:.1f}m²')

area()