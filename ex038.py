numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))

if numero1 > numero2:
    print('O primeiro valor "{}" é maior que o segundo valor "{}"'.format(numero1, numero2))

elif numero2 > numero1:
    print('O segundo valor "{}" é maior que o primeiro valor "{}"'.format(numero2, numero1))
else:
    print('Não existe valor maior, os dois são iguais')