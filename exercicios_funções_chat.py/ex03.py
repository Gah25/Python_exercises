def temp():
    print('=-' * 25)
    print('Bem vindo ao conversor de temperatura')
    print('=-' * 25)

    while True:

        print("""
    [ 0 ] SAIR
    [ 1 ] FAHRENHEIT
    [ 2 ] KELVIN """)
        
        try:
            opcao = int(input('Qual a opção: '))
            if opcao == 0:
                break

            if opcao <1 or opcao > 2:
                print('Digite uma opção válida')
                continue
                
            temperatura = float(input('Qual a temperatura: '))

            if opcao == 1:
                fahrenheit = (temperatura * 1.8) + 32
                print(f'{fahrenheit:.2f}° Fahrenheit')

            elif opcao == 2:
                kelvin = temperatura + 273.15
                print(f'{kelvin:.2f}° kelvin')
        
        except ValueError:
            print('ERRO! Digite um valor válido.')
temp()
