from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ORM import Pessoa

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

x = session.query(Pessoa).all()
#x = session.query(Pessoa).filter(Pessoa.nome == 'nelson').filter(Pessoa.nome == 'nelson')
x = session.query(Pessoa).filter_by(usuario = 'nelson', nome='nelson')

for i in x:
    print(i.id)