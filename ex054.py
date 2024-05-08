from datetime import date
data = date.today().year
maior_de_idade = 0
menor_de_idade = 0
for c in range(1, 8):
    ano_nascimento = int(input(f'Qual o ano de nascimento da {c}° pessoa: ')) 
    if data - ano_nascimento >= 21:
        maior_de_idade = maior_de_idade + 1
    else:
        menor_de_idade = menor_de_idade + 1
print(f'A Quantidade total de menores de idade é {menor_de_idade} e a Quantidade total de maiores de idade é {maior_de_idade} ')
