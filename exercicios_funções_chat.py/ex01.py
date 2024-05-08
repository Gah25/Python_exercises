def calculadora(): # adicao, divisao, multiplicacao, subtracao

        while True:
            print('''
[ 0 ] SAIR
[ 1 ] ADIÇÃO
[ 2 ] SUBTRAÇÃO
[ 3 ] MULTIPLICAÇÃO
[ 4 ] DIVISÃO ''')
            print()
            print('=-' * 25)
            
            opcao = int(input('Qual operação matemática você quer escolher? '))
            
            if opcao == 0:
                 break

            numero1 = float(input('Digite um número: '))
            numero2 = float(input('Digite outro número: '))

            if opcao == 1:
                adicao = numero1 + numero2
                print(f'A soma é: {adicao:.2f}')
            
            elif opcao == 2:
                subtracao = numero1 - numero2
                print(f'A subtração é: {subtracao:.2f}')
            
            elif opcao == 3:
                multiplicacao = numero1 * numero2
                print(f'A multiplicação é: {multiplicacao:.2f}')

            elif opcao == 4:
                if numero2 == 0:
                     print('Não é possivel dividir por zero')
                else:    
                    divisao = numero1 / numero2
                    print(f'A divisão é: {divisao:.2f}')

calculadora()