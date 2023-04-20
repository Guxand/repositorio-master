from teste import db

class Item(db.Model): # criamos e caracterizamos o banco de dados a partir de uma class que servirá de modelo ao SQL
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Item %r>' % self.name

class Usuario(db.Model):
    nome = db.Column(db.String(50), nullable=False)
    nickname = db.Column(db.String(20), primary_key=True)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Usuario %r>' % self.name