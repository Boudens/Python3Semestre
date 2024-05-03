import mysql.connector
conexao= mysql.connector.connect(user='root',password = '',host='127.0.0.1',database='db_loja_2')
print('Conexao:',conexao )
cursor = conexao.cursor()
#sql = "CREATE DATABASE if not exists db_loja_2"

'''
sql= CREATE TABLE IF NOT EXISTS tb_produtos(
        idt INT NOT NULL AUTO_INCREMENT,
        nome VARCHAR(45) NOT NULL,
        preco DECIMAL(4,2) NULL,
        dta_validade DATE NOT NULL,
        PRIMARY KEY (idt)
)'''

#sql = "INSERT INTO tb_produtos(nome,preco,dta_validade) VALUES('Pão',0.50,'2024-03-05')"
sql = "select * from tb_produtos"
cursor.execute(sql)
l_registros = cursor.fetchall()
print("-Lista de tuplas: ")

for i in l_registros:
    print(i)

#conexao.commit()
cursor.close()
conexao.close()
