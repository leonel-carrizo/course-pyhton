# # Funsion filter()
# lista = ['pepito', 'pedro', 'peras', 'pcarlos', 'carajito', '-']


# def iniciales(x):
#     if str(x).startswith('pe'):
#         return True
#     return False


# res = filter(iniciales, lista)
# res2 = filter(lambda x: str(x).startswith('pe'), ['pepito', 'pedro', 'peras', 'pcarlos', 'carajito', '-'] )
# print(list(res))
# print(list(res2))
# ---------------------------------------------------------

# Funsion map()
# def cuadrado(x):
#     return x * x


# resul = map(cuadrado, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# res = map(lambda x: x*x, [1, 2, 3, 4, 5, 6, ])
# print(list(resul))
# print(list(res))

# -----------------------------------------------------------------

# Funsion reduce(): se debe importar se encuentra en el modulo 'functools'
# from functools import reduce


# def suma(a, b):
#     print(f'a={a}, b={b}')
#     return a + b


# res = reduce(suma, [1, 2, 3, 4, 5])
# #res2 = reduce(lambda a, b: a + b, [1, 2, 3, 4, 5, 6])
# print(res)
# # print(res2)

# -----------------------------------------------------------

# Funsion zip() agerga interables en una tupla y los devuelve

# cursos = ['java', 'Python', 'Git']
# asistentes = [15, 20, 4]

# demo = zip(cursos, asistentes)
# print(list(demo))

# -------------------------------------------------------------

# all() y any(): Sirven para verificar que todas las condiciones de una lista se cumpla o alguian de las condiciones.

# listaA = [1 == 1, 2 == 2, 3 == 4]

# res = any(listaA)
# print(res)  # si al menos una de las condiciones es cierta retorna True

# res2 = all(listaA)
# print(res2)  # Si al menos una de las condiciones es falsa retornara FAlse

# -----------------------------------------------------------------

# Funsion round(): sirve para redondear

# a = 5.5
# b = 5.9
# c = 5.4

# print(round(a))
# print(round(b))
# print(round(c))

# ------------------------------------

# Funsion min(): devuelve el valor minimo de la lista

# print(min(1, 2, 3, 4, 5, 6, 7))

# -----------------------------------

# funsion pow(): devuelve un numero elevado a una exponente

# print(pow(2,4))

# ----------------------------------------


# from audioop import reverse


# lista = ['z', 'c', 'd', 'a']
# ordenada = sorted(lista, reverse=True, key=lambda x: str(x).startswith('a'))
# print(ordenada)

# from getpass import getpass

# user = input('User: ')
# passw = getpass('Password: ')

# print(user, passw)


