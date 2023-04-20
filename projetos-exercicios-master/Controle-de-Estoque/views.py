from teste import app, db
from flask import render_template, request, redirect, url_for, flash, session 
from models import Item, Usuario

#lista = Item.query.order_by(Item.id)

# rotas do site
@app.route('/') # rota estoque
def consultar_estoque():
    lista = Item.query.order_by(Item.id)
    return render_template('estoque.html', titulo='Estoque', estoque=lista)


@app.route('/consultar', methods=['POST',])
def consultar():
    item = request.form['consultar']
    item_consultado = Item.query.filter_by(item=item).first()

    if item_consultado:
        lista = Item.query.filter_by(item=item)
        return render_template('consultar.html', titulo='Estoque', estoque=lista)

    flash('O item consultado não existe.')
    return redirect(url_for('consultar_estoque'))


@app.route('/novo') # rota cadastrar novo item no estoque
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Cadastrar Item')


@app.route('/criar', methods=['POST',]) # rota para criar o item e adicionar no estoque
def criar():
    nitem = request.form['item']
    categoria = request.form['categoria']
    quantidade = request.form['quantidade']
    descricao = request.form['descricao']

    novo_item = Item(item=nitem, descricao=descricao,categoria=categoria, quantidade=quantidade)
    db.session.add(novo_item)
    db.session.commit()
    
    return redirect(url_for('consultar_estoque'))


@app.route('/editar/<int:id>') # rota editar item no estoque
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    item = Item.query.filter_by(id=id).first()
    return render_template('editar.html', titulo='Editando Item', item=item)


@app.route('/atualizar', methods=['POST',]) # rota para atualizar o item e adicionado no estoque
def atualizar():
    item_editado = Item.query.filter_by(id=request.form['id']).first()
    item_editado.item = request.form['item']
    item_editado.categoria = request.form['categoria']
    item_editado.quantidade = request.form['quantidade']
    item_editado.descricao = request.form['descricao']

    db.session.add(item_editado)
    db.session.commit()
    return redirect(url_for('consultar_estoque'))


@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))

    Item.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Item deletado com sucesso!')
    return redirect(url_for('consultar_estoque'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario = Usuario.query.filter_by(nickname=request.form['usuario']).first()
    if usuario:
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(f'Usuário {usuario.nickname} logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
        else:
            flash('Usuário não logado.')
            return redirect(url_for('login'))
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))
    

@app.route('/logout') # rota para fazer o logout
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso')
    return redirect(url_for('consultar_estoque'))