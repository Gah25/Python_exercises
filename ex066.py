contador = 0
soma = 0

while True:
    numero = int(input('Digite um valor (999 para parar): '))
    if numero == 999:
        break
    soma = soma + numero
    contador += 1
print(f'Foram digitados {contador} números e a soma é {soma}')