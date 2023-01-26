class Pessoas:
    possui_olhos = True
    possui_boca = True
    raca = 'Ser Humano'


    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def retorna_nome(self):
        return self.nome

    def logar_sistema(self):
        print(f'{self.retorna_nome()} Está logando no sistema')

    @classmethod
    def andar(cls):
        cls.possui_boca = False
        return None

    @staticmethod
    def e_adulto(idade):
        if idade > 18:
            return True
        return False
        

#p1 = Pessoas('Nelson Silva', 25)
#p2 = Pessoas('Silva Santos', 23)


print(Pessoas.e_adulto(21))
