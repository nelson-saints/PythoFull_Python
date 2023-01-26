import pickle
#serialização de dados em binarios

class Pessoa:
    nome = 'Nelson'
    idade = 25

class Pessoas:
    def __init__(self, nome, idade):
        self.nome= nome
        self.idade = idade

p1 = Pessoas('marcos', 21)

arq = open('arquivo.pkl', 'wb')
pickle.dump(p1, arq)


arq = open('arquivo.pkl', 'rb')
retornou = pickle.load(arq)

print(retornou.nome)