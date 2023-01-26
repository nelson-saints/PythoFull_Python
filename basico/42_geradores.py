from tkinter import Y
from pympler.asizeof import asizesof
#biblioteca utilizada para verificar a uantidade e memória utilizada pela linguem python

# #Função geradora - gasta menos memória
# def dobro(lista):
#     for i in lista:
#         yield i

# #Função comum - nao geradora - gasta muito mais memória
# def dobro2(lista):
#     lista_2 =[]
#     for i in lista:
#         lista_2.append(i)
#     return lista_2


# y = dobro2(range(0, 100000))
# x = dobro(range(0, 100000))

# print(asizesof(y))
# print(asizesof(x))


def dobro(lista):
    for i in lista:
        yield i*2


x = dobro(range(0, 100))

while True:
    try:   
        print(next(x))
    except StopIteration:
        break