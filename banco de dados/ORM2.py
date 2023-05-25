from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_
from ORM import Pessoa
from ORM import Produto

def RetornaSession():
    USUARIO = "root"
    SENHA = "123456"
    HOST = "localhost"
    BANCO = "aulapythonfull"
    PORT = "3308"
    CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

session = RetornaSession()

#Inserindo dados na tabela ----

x = Produto(id='1',
            categoria='frios')

# y = Pessoa(nome='amanda',
#            usuario='carolina',
#            senha='321654')



# session.add_all([y])
# session.rollback()


#Select

#x = session.query(Pessoa).all()
# for i in x:
#     print(i.nome)

#Operador AND
##x = session.query(Pessoa).filter(Pessoa.nome == 'nelson').filter(Pessoa.usuario == 'nelson')
# x = session.query(Pessoa).filter_by(usuario = 'nelson', nome = 'nelson')
# for i in x:
#     print(i.id)



#Operador OR
# x = session.query(Pessoa).filter(or_(Pessoa.nome =='nelson', Pessoa.usuario == 'carolina')).all()
# print(x)
# for i in x:
#     print(i.id)


# #Update
# x = session.query(Pessoa).filter(Pessoa.id == 3).all()
# x[0].nome = 'Gabriel'
# x[0].senha = '1234'
# print(x[0].id)


# #Delete
# x = session.query(Pessoa).filter(Pessoa.id == 3).delete() #Deleta toda linha

# x = session.query(Pessoa).filter(Pessoa.id == 3).one()
# session.delete(x) # deleta a linha digitada


session.commit()