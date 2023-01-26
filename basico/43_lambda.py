# import os

# x = lambda: os.system('cls')

# y = lambda *idade: print(idade)

# y('nelson', '25', 'silva')

def teste():
    return lambda *idade: print(idade)

x = teste()

x('nelson', 'marcos')