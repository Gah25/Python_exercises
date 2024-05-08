"""
JEITO QUE EU FIZ

while True:
    print('-' * 38)
    numero = int(input('Quer ver a tabuada de qual valor: ')) 
    print('-' * 38)

    if numero <= 0:
        print('PROGRAMA ENCERRADO')
        break
    
    contador = 0
    while contador < 10:
        contador += 1
        soma = contador * numero
    
        print(f'|{numero} x {contador} = {soma}|')"""

################################################################

# JEITO PROFESSOR GUANABARA

while True:
    print('-' * 38)
    numero = int(input('Quer ver a tabuada de qual valor: ')) 
    
    if numero < 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break

    for contador in range(1, 11):
        print(f'|{numero} x {contador} = {numero * contador}|')
    print('-' * 38)