#Receba um número inteiro do usuário e mostre a tabuada desse número

n1 = int(input('Digite um valor: '))
i = 0
while i <= 10:
    print(f'{n1} X {i} = {n1 * i}')
    i += 1