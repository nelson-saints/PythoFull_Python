class Animal:
    def andar(self):
        print('Estou andando como um animal')

    def correr(self):
        print('Estou correndo')

    def pular(self):
        print('Estou pulando')

class Felino():
    def felino(self):
        print('eu sou um felino')

    def andar(self):
        print('Estou andando como um felino')

class Cachorro(Animal):
    def latir(self):
        print('Estou latindo')

class Gato(Felino, Animal):
    def miar(self):
        print('Estou andando como um gato')
    


y = Gato()
y.andar()