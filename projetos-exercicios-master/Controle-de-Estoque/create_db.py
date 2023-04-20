from errno import errorcode
from teste import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Item(db.Model): # criamos e caracterizamos o banco de dados a partir de uma class que servirá de modelo ao SQL
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item = db.Column(db.String(50))
    descrição = db.Column(db.String(200))
    quantidade = db.Column(db.Integer)

    def __repr__(self):
        return '<Item %r>' % self.nome

class Usuario(db.Model):
    nome = db.Column(db.String(50))
    nickname = db.Column(db.String(20), primary_key=True)
    senha = db.Column(db.String(100))

    def __repr__(self):
        return '<Usuario %r>' % self.nome
    




conn = 'postgresql://postgres:game2610@localhost/estoque'

'''print("Conectando...")
try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='admin'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)'''

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `estoque`;")

cursor.execute("CREATE DATABASE `estoque`;")

cursor.execute("USE `estoque`;")

# criando tabelas
TABLES = {}
TABLES['Item'] = ('''
      CREATE TABLE `item` (
      `id` integer NOT NULL AUTO_INCREMENT,
      `item` varchar(50) NOT NULL,
      `descricao` varchar(200) NOT NULL,
      `quantidade` integer NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Usuarios'] = ('''
      CREATE TABLE `usuarios` (
      `nome` varchar(50) NOT NULL,
      `nickname` varchar(20) NOT NULL,
      `senha` varchar(100) NOT NULL,
      PRIMARY KEY (`nickname`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except conn.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')


# inserindo usuarios
usuario_sql = 'INSERT INTO usuarios (nome, nickname, senha) VALUES (%s, %s, %s)'
usuarios = [
      ("Igor Silva", "igor123", "propagar"),
      ("Maurivan Giehl", "mauri123", "propagar"),
      ("Yuri Welter", "yuri123", "propagar")]
cursor.executemany(usuario_sql, usuarios)

cursor.execute('select * from estoque.usuarios')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])



# inserindo itens
jogos_sql = 'INSERT INTO item (item, descricao, quantidade) VALUES (%s, %s, %s)'
jogos = [
      ('Luva', 'Luva de Borracha amarela', '15'),
      ('Saco de Cimento', 'Cimento 10kg', '20'),
      ('Martelo', 'Martelo emborrachado 2kg', '28'),
      ('Furadeira', 'Furadeira Laranja', '10'),
      ('Tijolo', 'Tijolo 6 furos', '2'),]
cursor.executemany(jogos_sql, jogos)

cursor.execute('select * from estoque.item')
print(' -------------  Itens:  -------------')
for jogo in cursor.fetchall():
    print(jogo[1])

# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()
