#Receba 3 números inteiros e exiba o maior deles.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

if n1 > n2 and n1 > n3:
    print(f'O maior numero digita é: {n1}')
elif n2 > n1 and n2 > n3:
    print(f'O maior numero digita é: {n2}')
else:
    print(f'O maior numero digita é: {n3}')

