import sqlite3
database = 'Livraria.db'
conexao = sqlite3.connect(database)
cur = conexao.cursor()
sql = "insert into  tb_cliente(cpf, nome) values('678','Irivin')"
cur.execute(sql)
conexao.commit()
cur.close()
conexao.close()
print("Fechou a base de dados")
