from math import pow
peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))

imc = peso / pow(altura, 2) 

if imc < 18.5:
    print(f'Seu IMC é {imc:.2f} -> Você está abaixo do peso')
elif imc > 18.5 and imc < 26:
    print(f'Seu IMC é {imc:.2f} -> Você está no peso ideal')
elif imc > 25 and imc < 31:
    print(f'Seu IMC é {imc:.2f} -> Sobrepeso')
elif imc > 30 and imc < 41:
    print(f'Seu IMC é {imc:.2f} -> Obesidade')
else:
    print(f'Seu IMC é {imc:.2f} -> Obesidade mórbida')