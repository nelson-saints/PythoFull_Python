#Receba um número e mostre todos os números pares de 0 até o número digitado.

from re import I


n1 = int(input('Digite um número: '))
i = 0
while i <= n1:
    if i % 2 == 0:
        print(i)
    i += 1