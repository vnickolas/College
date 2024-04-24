import mysql.connector


conexao = mysql.connector.connect(
    host='localhost',
    username='root',
    password='Mnickol@s1983',
    database='sucos_vendas'
)

print('Conexão com sucesso')

cursor = conexao.cursor()

comando = 

cursor.execute(comando)




cursor.close()
conexao.close()
