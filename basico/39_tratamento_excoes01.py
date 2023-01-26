try:
    X = int(input('Digite um número: '))
    print(5/X)
except ValueError:
    print('Digite um número inteiro!')
except ZeroDivisionError:
    print('Não digite 0!')