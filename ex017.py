import math
cateto_oposto = float(input('Digite o valor do cateto oposto: ')) 
cateto_adjacente = float(input('Digite o valor do cateto adjacente: ')) 


co = math.pow(cateto_oposto, 2)
ca = math.pow(cateto_adjacente, 2)
soma = co + ca

hipotenusa = math.sqrt(soma)

print(f'A hipotenusa de {soma} é igual a {hipotenusa}')