import sqlite3
from IPython.display import display
import pandas as pd
from tabulate import tabulate
conexao = sqlite3.connect('livraria.db')
cur = conexao.cursor()
sql = "select * from tb_cliente"
cur.execute(sql)
l_registros = cur.fetchall()
print(l_registros)
cur.close()
conexao.close()
print("Fechou a base de dados")

df = pd.DataFrame(l_registros)
print(tabulate(df, headers = 'keys', tablefmt = 'psql'))
