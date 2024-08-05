from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# @app.get("/home")
# def root():
#      return{'mensagem': 'Olá Mundo, Minha API!!!'}

# @app.get("/cadastro")
# def cadastro():
#      return{'mensagem': 'Cadastro'}
 

# @app.get("/login")
# def login():
#      return{'mensagem': 'Login'}

class Usuario(BaseModel):
     id: int
     nome:str
     senha:str
     
lista = [
     Usuario(id=1, nome='Nelson', senha='minhasenha1'),
     Usuario(id=2, nome='caio', senha='minhasenha2'),
     Usuario(id=3, nome='joao', senha='minhasenha3')  
]

@app.post('/usuario')
def main(usuario: Usuario):
     lista.append(usuario)
     return "usuario cadastrado"

@app.get('/usuarioListar')
def main():
     return lista