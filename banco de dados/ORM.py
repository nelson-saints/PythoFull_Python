from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, ForeignKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USUARIO = "root"
SENHA = "123456"
HOST = "localhost"
BANCO = "aulapythonfull"
PORT = "3308"

CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

engine = create_engine(CONN, echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Pessoa(Base):
    __tablename__ = "Pessoa"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50))
    usuario = Column(String(20))
    senha = Column(String(10))


class Categoria(Base):
    __tablename__ = "categoria"
    id = Column(Integer, primary_key=True, autoincrement=True)
    categoria = Column(String(50))
    


class Produto(Base):
    __tablename__ = "produto"
    id = Column(Integer, primary_key=True, autoincrement=True)
    produto = Column(String(50))
    quantidade = Column(Integer)
    categoria_id = Column(Integer, ForeignKey('categoria.id'))

Base.metadata.create_all(engine)