"""
# JEITO QUE EU FIZ

from datetime import date

def voto():
    data = date.today().year
    ano_nascimento = int(input('Em que ano você nasceu? '))
    idade = data - ano_nascimento

    if idade >= 16 and idade < 18:
        print(f'Com {idade} anos: VOTO OPCIONAL')
    
    elif idade >= 18 and idade < 70:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')

    elif idade >= 70: 
        print(f'Com {idade} anos: VOTO OPCIONAL')
    
    elif idade < 16:
        print(f'Com {idade} anos: VOTO NEGADO')

voto()
"""

# PROFESSOR GUANABARA

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

nascimeto = int(input('Em que ano você nasceu? '))
print(voto(nascimeto))
