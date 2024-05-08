"""
# JEITO PROFESSOR GUANABARA

# def fatorial(numero, show):
#     """
#     -> Calcula o fatorial de um número.
#     :param n: O número a ser calculado.
#     :param show: (opcional) Mostrar ou não a conta.
#     :return: O valor do Fatorial de um número n.
#     """
#     f = 1
#     for c in range(numero, 0, -1):
#         if show == True:
#             print(c, end='')
#             if c > 1:
#                 print(' x ', end='')
#             else:
#                 print(' = ', end='')
#         f *= c
#     return f

# # Programam Principal
# print(fatorial(1000, show=True))
# help(fatorial)



#################################################




# JEITO QUE EU FIZ





def fatorial(numero, show):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    contador = numero
    f = 1

    while contador > 0:
        if show:
            print(contador, end='')
            if contador > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f= f * contador
        contador -= 1
    return f

print(fatorial(5, show=True))
help(fatorial)