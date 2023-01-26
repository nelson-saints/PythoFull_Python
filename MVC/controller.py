from dal import PessoaDal
from model import Pessoa

class pessoaController:
    @classmethod
    def cadastrar(cls, nome, idade: int):
        #len(nome) > 2 and (idade > 0 and idade < 200) and len(cpf) == 11:
        if len(nome) > 2 and (idade > 0 and idade < 200):
            try:
                PessoaDal.salvar(Pessoa(nome, idade))
                return True
            except:
                return False
        else:
            return False

    @classmethod
    def cadastrar_cpf(cls, cpf):
        if len(cpf) == 11:
            try:
                PessoaDal.salvar(Pessoa(cpf))
                return True
            except:
                return False
        else:
            return False

        

