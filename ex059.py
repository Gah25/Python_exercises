from time import sleep

valor1 = int (input('Escolha o primeiro valor: '))
valor2 = int (input('Escolha o segundo valor: '))

opcao = 0
while opcao != 5:
    
    print("""
[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA
""")
    
    opcao = int (input('Qual a sua opção? '))

    if opcao == 1:
        soma = valor1 + valor2
        print(f'A soma entre o {valor1} + {valor2} é = {soma}')

    elif opcao == 2:
        multiplicacao = valor1 * valor2
        print(f'A multiplicação entre o {valor1} x {valor2} é = {multiplicacao}')

        

    elif opcao == 3:
        if valor1 > valor2:
            print(f'O {valor1} é maior que o {valor2}')
        elif valor1 == valor2:
            print(f'O {valor1} é igual ao {valor2}')
        else:
            print(f'O {valor2} é maior que o {valor1}')


    elif opcao == 4:
        print('Informe os números novamente')
        valor1 = int (input('Escolha o primeiro valor: '))
        valor2 = int (input('Escolha o segundo valor: '))

    elif opcao == 5:
        print('Finalizando... ')
        sleep(2)
    
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
print('Fim do programa! Volte sempre!')