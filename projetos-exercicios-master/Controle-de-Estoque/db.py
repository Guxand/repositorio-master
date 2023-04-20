from sqlalchemy import create_engine


engine = create_engine('postgresql://postgres:game2610@localhost/estoque')

conn = engine.connect()


create_item = '''create table item(
    id serial NOT NULL,
    item varchar(50) Not null,
    descricao varchar(200) not null,
    categoria varchar(50) not null,
    quantidade integer not null,
    constraint pk_item primary key (id))'''

create_usuario = '''create table usuario(
    nome varchar(50) Not null,
    nickname varchar(20) Not null,
    senha varchar(100) not null,
    constraint pk_usuario primary key (nickname))'''

#conn.execute(create_item)
#conn.execute(create_usuario)

insert_usuario = '''insert into usuario (nome, nickname, senha) VALUES ('Igor Douglas Ramos da Silva', 'igordrsilva', 'game2610')'''

#conn.execute(insert_usuario)

insert_itens = '''INSERT INTO item (item, descricao, quantidade, categoria) VALUES
        ('Luva', 'Luva de Borracha amarela', 15, 'Segurança'),
        ('Saco de Cimento', 'Cimento 10kg', 20, 'Produção'),
        ('Martelo', 'Martelo emborrachado 2kg', 28, 'Produção'),
        ('Furadeira', 'Furadeira Laranja', 10, 'Produção'),
        ('Tijolo', 'Tijolo 6 furos', 2, 'Produção')'''

#conn.execute(insert_itens)


usuarios = conn.execute("SELECT * FROM usuario")
print(' -------------  Usuários:  -------------')
for user in usuarios.fetchall():
    print(f'{user[0]} | {user[1]}')

itens = conn.execute('SELECT * FROM item')
print('\n -------------  Itens:  -------------')
for item in itens.fetchall():
    print(f'{item[0]} | {item[1]} | {item[4]}')

conn.close()
conn.close()
