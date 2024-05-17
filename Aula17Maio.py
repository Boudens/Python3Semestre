import mysql.connector
from IPython.display import display
import pandas as pd

def create_database():
    conexao = mysql.connector.connect(user='root',password='',host='127.0.0.1')
    print("Conexao feita:",conexao)
    cursor = conexao.cursor()
    sql="CREATE DATABASE IF NOT EXISTS db_cadastro"
    cursor.execute(sql)
    cursor.close()
    print("Conexão fechada")

def create_connection():
    con = mysql.connector.connect(user='root',password='',host='127.0.0.1',database='db_cadastro')
    print("Conexão:",con)
    return con

def create_table():
    sql_cargo= """ CREATE TABLE IF NOT EXISTS tb_cargo(
    idt INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(45) UNIQUE NOT NULL,
    PRIMARY KEY (idt)
    )"""
    cursor.execute(sql_cargo)
    sql_empregado="""CREATE TABLE IF NOT EXISTS tb_empregado(
    idt INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(45) NOT NULL,
    data_nascimento date NULL,
    genero enum('M','F') NOT NULL,
    cod_cargo int NOT NULL,
    PRIMARY KEY (idt),
    FOREIGN KEY(cod_cargo) REFERENCES tb_cargo(idt)
    )
    """
    cursor.execute(sql_empregado)

def insert_cargo():
    a_nome = input('Nome do cargo: ')
    sql=f"""INSERT INTO tb_cargo (nome)
        values('{a_nome}')"""
    cursor.execute(sql)
    conexao.commit()

def insert_empregado():
    a_nome = input('Nome do empregado: ')
    a_data = input('Data de nascimento (yyyy-mm-dd): ')
    a_genero = input('Genero (M,F): ')
    a_codCargo = int(input('Codigo do cargo: '))
    sql=f"""INSERT INTO tb_empregado (nome,data_nascimento,genero,cod_cargo)
        values('{a_nome}','{a_data}','{a_genero}','{a_codCargo}')"""
    cursor.execute(sql)
    conexao.commit()
    
def select_empregados():
    sql="select * from db_cadastro.tb_empregado"
    cursor.execute(sql)
    l_registros = cursor.fetchall()
    for registro in l_registros:
        print("IDT:",registro[0],"| Nome",registro[1],"| Data de Nascimento:",registro[2],"| Genero:",registro[3],"| Cod. Cargo:",registro[4])


def select_empregados2():
    sql="select * from db_cadastro.tb_empregado"
    cursor.execute(sql)
    l_registros = cursor.fetchall()
    df = pd.DataFrame(l_registros)
    display(df)

def close_connection():
    cursor.close()
    conexao.close()
    print("Conexão fechada")


if __name__ == "__main__":
    create_database()
    conexao = create_connection()
    cursor = conexao.cursor()
    create_table()
    #insert_cargo()
    #insert_empregado()
    #select_empregados()
    select_empregados2()
    close_connection()
