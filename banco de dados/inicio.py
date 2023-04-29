import pymysql.cursors

con = pymysql.connect(
    host="localhost",
    user="root",
    password="123456",
    port=3308,
    db="aulapythonfull",
    charset="utf8mb4",
    cursorclass = pymysql.cursors.DictCursor)

def criaTabela(nomeTabela):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"create table {nomeTabela} (nome varchar(50), CPF decimal(15))")
        print("tabela criada com sucesso")
    except Exception as e:
        print(f'Ocorreu um erro {e}')

def removeTabela(nomeTabela):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"drop table {nomeTabela}")
        print("tabela removida com sucesso")
    except Exception as e:
        print(f'Ocorreu um erro {e}')

def insereTabela(nome, CPF):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"insert into teste values ('{nome}','{CPF}')")
            con.commit()
        print("valor inserido com sucesso")
    except Exception as e:
        print(f'Ocorreu um erro {e}')

def imprimeDados(tabela):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {tabela}")
            resultado = cursor.fetchall()
            for i in resultado:
                print(i)
    except Exception as e:
        print(f'Ocorreu um erro {e}')

def atualizaDado(tabela):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"UPDATE {tabela} SET nome='Nelson Silva' WHERE nome = 'Silva'")
            print('Dado alterado com sucesso')
    except Exception as e:
        print(f'Ocorreu um erro {e}')

def deletDados(tabela):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"DELETE FROM {tabela} WHERE nome = 'Caio'")
            print('Delete efetuado com sucesso')
    except Exception as e:
        print(f'Ocorreu um erro {e}')


deletDados("teste")

con.commit()
con.close()