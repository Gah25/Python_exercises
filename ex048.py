soma = 0 # ISSO É CHAMADO DE -> ACUMULADOR
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c # soma += c
        contador = contador + 1 # contador += 1
print(f'A soma de todos os {contador} valores solicitados é {soma}')
    