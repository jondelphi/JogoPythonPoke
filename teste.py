import sqlite3

conexao = sqlite3.connect('bdgame.db')
cursor = conexao.cursor()
consulta = """SELECT * FROM recorde ORDER BY pontos DESC"""

cursor.execute(consulta)

recorde = cursor.fetchall()



for r in recorde:
    print(f"{r[1]} | {r[2]} | Pegou: {r[3]:>4} |")
    print("-"*34)
conexao.close()
