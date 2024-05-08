
# JEITO QUE EU FIZ

nota = {}
nota['Nome'] = str(input('Nome: '))
nota['Média'] = float(input(f'Média de {nota["Nome"]}: ')) 
print('-=' * 30)
for k, v in nota.items():
    print(f'  - {k} é igual a {v}')
if nota['Média'] >= 7:
    print("  - Situação é igual a aprovado")
elif nota['Média'] < 7 and nota['Média'] >= 5:
    print("  - Situação é igual a Recuperação")
else:
    print("  - Situação é igual a reprovado") 


########################################################
# PROFESSOR GUANABARA

# aluno = {}
# aluno['Nome'] = str(input('Nome: '))
# aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: ')) 
# print('-=' * 30)
# if aluno['Média'] >= 7:
#     aluno['Situação'] = 'Aprovado'
# elif aluno['Média'] < 7 and aluno['Média'] >= 5:
#     aluno['Situação'] = 'Recuperação'
# else:
#     aluno['Situação'] = 'Reprovado'

# print('-=' * 30)
# for k, v in aluno.items():
#     print(f'  - {k} é igual a {v}')