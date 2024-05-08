
numero = int(input('Digite um número para ver sua tabuada: '))
contador = 0
for c in range(1, 11):
    contador += 1  # contador = contador + 1
    soma = numero * contador
    print(f'|{numero} x {contador} = {soma}|')
