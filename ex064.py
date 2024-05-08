
# JEITO QUE EU FIZ

parada = 0
contador = 0
soma = 0

while parada != 999:
    numero = int(input('Digite um número [999 para parar]: '))
    contador += 1
    soma = soma + numero
    if numero != 999:
        print(end='') # OU utilizar 'pass'
    else:
        contador -= 1
        parada = 999
        soma = soma - numero
        
print(f'Você digitou {contador} números')   
print(f'A soma entre os números escolhido é: {soma}')   


#########################################################################

"""# PROFESSOR GUANABARA

# POSSO FAZER ASSIM -> numero = contador = soma = 0
numero = 0
contador = 0
soma = 0

numero = int(input('Digite um número [999 para parar]: '))
while numero != 999:
    soma += numero
    contador += 1
    numero = int(input('Digite um número [999 para parar]: ')) # FLAG como ultima linha, ele vai desconsiderar o 999 e não vai adicionar a soma

print('Você digitou {} números e a soma entre eles foi {}'. format(contador, soma))"""