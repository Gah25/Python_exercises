def calcular_fatorial(numero):
    fat = 1
    for i in range(2, numero + 1):
        fat *= i
    return fat

def fatorial():
    numero = int(input(f'Digite o valor que vai ser fatorado: '))
    if numero < 0:
        print('O fatorial não é definido para números negativos.')
        return
        
    resultado = calcular_fatorial(numero)    
    print(f'O fatorial de {numero} é: {resultado}')

fatorial()