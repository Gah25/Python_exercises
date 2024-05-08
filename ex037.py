numero = int (input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] converter para BINÁRIO)
[ 2 ] converter para OCTAL)
[ 3 ] converter para HEXADECIMAL ''')
opcao = int(input('Escolha sua opção: '))

if opcao == 1:
    print(f'{numero} convertido para BINÁRIO é igual a {bin(numero)[2:]}') # bin mostra o número em binario

elif opcao == 2:
    print(f'{numero} convertido para OCTAL é igual a {oct(numero)[2:]}') # oct mostra o número em OCTAL

elif opcao == 3:
    print(f'{numero} convertido para HEXADECIMAL é igual a {hex(numero)[2:]}') # hex mostra o número em HEXADECIMAL

else:
    print('Digite uma opção válida. Tente novamente! ')