# def soma_numeros(*args):
#     #print(f'n1 = {n1} n2 = {n2} args = {args}')
#     soma = 0
#     for i in args:
#         soma += i
#     print(soma)

# soma_numeros(2, 6, 1, 2, 3)


def soma_numeros(**kwargs):
    X = kwargs.get('teste4')
    if X:
        print('foi passado')
    else:
        print('Não foi passado')

soma_numeros(teste1 = 1, teste2 = 2, teste3 = 3, teste4 = 4)