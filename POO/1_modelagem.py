# class Pessoas:
#     def __init__(self, nome, idade, cpf):
#         self.nome = nome
#         self.idade = idade
#         self.cpf = cpf

#     def logar_sistema(self):
#         print(f'{self.nome} está logando no sistema')
    

# p1 = Pessoas('Nelson Silva', 25, '4631274458')
# p1.logar_sistema()



class Pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def retorna_nome(self):
        return self.nome

    def logar_sistema(self):
        print(f'{self.retorna_nome()} Está logando no sistema')

p1 = Pessoas('Nelson Silva', 25)

p1.logar_sistema()
#Self referencia uma instancia. -'_'- 

