
#from crypt import methods
from os import abort
from flask import Flask, flash, redirect, render_template, request, url_for, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user


# main = Blueprint('main', __name__)
# auth = Blueprint('auth', __name__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5432/imobiliaria"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config['SECRET_KEY'] = "random string"
# app.register_blueprint(auth)
# app.register_blueprint(main)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(100), unique=True)
    senha = db.Column(db.String(100))
    nome = db.Column(db.String(1000))

class Cliente(db.Model):
  __tablename__ = 'clientes'

  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String())
  cpf_cnpj = db.Column(db.String())
  tipo_pessoa = db.Column(db.String())
  endereco = db.Column(db.String())
  cidade = db.Column(db.String())
  estado = db.Column(db.String())
  cep = db.Column(db.String())
  telefone = db.Column(db.String())
  email = db.Column(db.String())
  contratos = db.relationship('Contrato', backref='cliente', lazy=True)

  def __init__(self, nome, cpf_cnpj, tipo_pessoa, endereco, cidade, estado, cep, telefone, email):
    self.nome = nome
    self.cpf_cnpj = cpf_cnpj
    self.tipo_pessoa = tipo_pessoa
    self.endereco = endereco
    self.cidade = cidade
    self.estado = estado
    self.cep = cep
    self.telefone = telefone
    self.email = email
  
  def __repr__(self):
    return f"{self.nome}"

  @app.route('/clientes', methods=['POST', 'GET'])
  def handle_clientes():
    if request.method == 'POST':
      if request.is_json:
        data = request.get_json()
        novo_cliente = Cliente(nome=data['nome'], cpf_cnpj=data['cpf_cnpj'], tipo_pessoa=data['tipo_pessoa'], endereco=data['endereco'], cidade=data['cidade'], estado=data['estado'], cep=data['cep'], telefone=data['telefone'], email=data['email'])
        db.session.add(novo_cliente)
        db.session.commit()
        return {'Mensagem': f"Cliente {novo_cliente.nome} foi criado com sucesso."}
      else:
        return {"Erro": "A requesição não foi carregada no formato JSON."}
    
    elif request.method == 'GET':
      clientes = Cliente.query.all()
      results = [
        {
          'nome': cliente.nome,
          'cpf_cnpj': cliente.cpf_cnpj,
          'tipo_pessoa': cliente.tipo_pessoa,
          'endereco': cliente.endereco,
          'cidade': cliente.cidade,
          'estado': cliente.estado,
          'cep': cliente.cep,
          'telefone': cliente.telefone,
          'email': cliente.email,
          'id': cliente.id
        } for cliente in clientes
      ]

      return {"Total de Cliente": len(results), "clientes": results}

  @app.route('/clientes/<cliente_id>', methods=['GET', 'PUT', 'DELETE'])
  def handle_cliente(cliente_id):
    cliente = Cliente.query.get_or_404(cliente_id)
    if request.method == 'GET':
      response = {
          'nome': cliente.nome,
          'cpf_cnpj': cliente.cpf_cnpj,
          'tipo_pessoa': cliente.tipo_pessoa,
          'endereco': cliente.endereco,
          'cidade': cliente.cidade,
          'estado': cliente.estado,
          'cep': cliente.cep,
          'telefone': cliente.telefone,
          'email': cliente.email,
          'id': cliente.id
      }
      return {"Mensagem": "Sucesso", "cliente": response}
    
    elif request.method == 'PUT':
      data = request.get_json()
      cliente.nome = data['nome']
      cliente.cpf_cnpj = data['cpf_cnpj']
      cliente.tipo_pessoa = data['tipo_pessoa']
      cliente.endereco = data['endereco']
      cliente.cidade=data['cidade']
      cliente.estado=data['estado']
      cliente.cep=data['cep']
      cliente.telefone=data['telefone']
      cliente.email=data['email']
      db.session.add(cliente)
      db.session.commit()
      return {"Mensagem": f"Cliente {cliente.nome} atualizado com sucesso!"}
    
    elif request.method == 'DELETE':
      db.session.delete(cliente)
      db.session.commit()
      return {"Mensagem": f"Cliente {cliente.nome} deletado com sucesso!"}
 

class Corretor(db.Model):
  __tablename__ = 'corretores'

  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String())
  cpf_cnpj = db.Column(db.String())
  tipo_pessoa = db.Column(db.String())  
  telefone = db.Column(db.String())
  email = db.Column(db.String())
  contratos = db.relationship('Contrato', backref='corretor', lazy=True)

  def __init__(self, nome, cpf_cnpj, tipo_pessoa,telefone, email):
    self.nome = nome
    self.cpf_cnpj = cpf_cnpj
    self.tipo_pessoa = tipo_pessoa
    self.telefone = telefone
    self.email = email
  
  def __repr__(self):
    return f"Nome: {self.nome}"

  @app.route('/corretores', methods=['POST', 'GET'])
  def handle_corretores():
    if request.method == 'POST':
      if request.is_json:
        data = request.get_json()
        novo_corretor = Corretor(nome=data['nome'], cpf_cnpj=data['cpf_cnpj'], tipo_pessoa=data['tipo_pessoa'], telefone=data['telefone'], email=data['email'])
        db.session.add(novo_corretor)
        db.session.commit()
        return {'Mensagem': f"Corretor {novo_corretor.nome} foi criado com sucesso."}
      else:
        return {"Erro": "A requesição não foi carregada no formato JSON."}
    
    elif request.method == 'GET':
      corretores = Corretor.query.all()
      results = [
        {
          'nome': corretor.nome,
          'cpf_cnpj': corretor.cpf_cnpj,
          'tipo_pessoa': corretor.tipo_pessoa,          
          'telefone': corretor.telefone,
          'email': corretor.email,
          'id': corretor.id
        } for corretor in corretores
      ]

      return {"Total de Corretores": len(results), "corretores": results}

  @app.route('/corretores/<corretor_id>', methods=['GET', 'PUT', 'DELETE'])
  def handle_corretor(corretor_id):
    corretor = Corretor.query.get_or_404(corretor_id)
    if request.method == 'GET':
      response = {
          'nome': corretor.nome,
          'cpf_cnpj': corretor.cpf_cnpj,
          'tipo_pessoa': corretor.tipo_pessoa,
          'telefone': corretor.telefone,
          'email': corretor.email,
          'id': corretor.id
      }
      return {"Mensagem": "Sucesso", "corretor": response}
    
    elif request.method == 'PUT':
      data = request.get_json()
      corretor.nome = data['nome']
      corretor.cpf_cnpj = data['cpf_cnpj']
      corretor.tipo_pessoa = data['tipo_pessoa']
      corretor.telefone=data['telefone']
      corretor.email=data['email']
      db.session.add(corretor)
      db.session.commit()
      return {"Mensagem": f"Corretor {corretor.nome} atualizado com sucesso!"}
    
    elif request.method == 'DELETE':
      db.session.delete(corretor)
      db.session.commit()
      return {"Mensagem": f"Corretor {corretor.nome} deletado com sucesso!"}

class Proprietario(db.Model):
  __tablename__ = 'proprietarios'

  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String())
  cpf_cnpj = db.Column(db.String())
  tipo_pessoa = db.Column(db.String())
  endereco = db.Column(db.String())
  cidade = db.Column(db.String())
  estado = db.Column(db.String())
  cep = db.Column(db.String())
  telefone = db.Column(db.String())
  email = db.Column(db.String())  
  imoveis = db.relationship('Imovel', backref='proprietario', lazy=True)

  def __init__(self, nome, cpf_cnpj, tipo_pessoa, endereco, cidade, estado, cep, telefone, email):
    self.nome = nome
    self.cpf_cnpj = cpf_cnpj
    self.tipo_pessoa = tipo_pessoa
    self.endereco = endereco
    self.cidade = cidade
    self.estado = estado
    self.cep = cep
    self.telefone = telefone
    self.email = email
  
  def __repr__(self):
    return f"Nome: {self.nome}"

  @app.route('/proprietarios', methods=['POST', 'GET'])
  def handle_proprietarios():
    if request.method == 'POST':
      if request.is_json:
        data = request.get_json()
        novo_proprietario = Proprietario(nome=data['nome'], cpf_cnpj=data['cpf_cnpj'], tipo_pessoa=data['tipo_pessoa'], endereco=data['endereco'], cidade=data['cidade'], estado=data['estado'], cep=data['cep'], telefone=data['telefone'], email=data['email'])
        db.session.add(novo_proprietario)
        db.session.commit()
        return {'Mensagem': f"Proprietário {novo_proprietario.nome} foi criado com sucesso."}
      else:
        return {"Erro": "A requesição não foi carregada no formato JSON."}
    
    elif request.method == 'GET':
      proprietarios = Proprietario.query.all()
      results = [
        {
          'nome': proprietario.nome,
          'cpf_cnpj': proprietario.cpf_cnpj,
          'tipo_pessoa': proprietario.tipo_pessoa,
          'endereco': proprietario.endereco,
          'cidade': proprietario.cidade,
          'estado': proprietario.estado,
          'cep': proprietario.cep,
          'telefone': proprietario.telefone,
          'email': proprietario.email,
          'id': proprietario.id,
          'imoveis': [
            {
              'descricao_imovel': imovel.descricao_imovel,
              'id': imovel.id,
            } for imovel in proprietario.imoveis
          ]
        } for proprietario in proprietarios
      ]

      return {"Total de Proprietarios": len(results), "proprietarios": results}

  @app.route('/proprietarios/<proprietario_id>', methods=['GET', 'PUT', 'DELETE'])
  def handle_proprietario(proprietario_id):
    proprietario = Proprietario.query.get_or_404(proprietario_id)
    if request.method == 'GET':
      response = {
          'nome': proprietario.nome,
          'cpf_cnpj': proprietario.cpf_cnpj,
          'tipo_pessoa': proprietario.tipo_pessoa,
          'endereco': proprietario.endereco,
          'cidade': proprietario.cidade,
          'estado': proprietario.estado,
          'cep': proprietario.cep,
          'telefone': proprietario.telefone,
          'email': proprietario.email,
          'id': proprietario.id
      }
      return {"Mensagem": "Sucesso", "proprietario": response}
    
    elif request.method == 'PUT':
      data = request.get_json()
      proprietario.nome = data['nome']
      proprietario.cpf_cnpj = data['cpf_cnpj']
      proprietario.tipo_pessoa = data['tipo_pessoa']
      proprietario.endereco = data['endereco']
      proprietario.cidade=data['cidade']
      proprietario.estado=data['estado']
      proprietario.cep=data['cep']
      proprietario.telefone=data['telefone']
      proprietario.email=data['email']
      db.session.add(proprietario)
      db.session.commit()
      return {"Mensagem": f"Proprietário {proprietario.nome} atualizado com sucesso!"}
    
    elif request.method == 'DELETE':
      db.session.delete(proprietario)
      db.session.commit()
      return {"Mensagem": f"Proprietário {proprietario.nome} deletado com sucesso!"}

class Imovel(db.Model):
  __tablename__ = 'imoveis'

  id = db.Column(db.Integer, primary_key=True)
  endereco = db.Column(db.String())
  cidade = db.Column(db.String())
  estado = db.Column(db.String())
  cep = db.Column(db.String())
  tipo_imovel = db.Column(db.String())
  descricao_imovel = db.Column(db.String())
  id_proprietario = db.Column(db.Integer, db.ForeignKey('proprietarios.id'), nullable=False) #Preencher corretamente
  contratos = db.relationship('Contrato', backref='imovel', lazy=True)
 

  def __init__(self, endereco, cidade, estado, cep, tipo_imovel, descricao_imovel, id_proprietario):
    self.endereco = endereco
    self.cidade = cidade
    self.estado = estado
    self.cep = cep
    self.tipo_imovel = tipo_imovel
    self.descricao_imovel = descricao_imovel
    self.id_proprietario = id_proprietario
  
  def __repr__(self):
    return f"ID: {self.id} - Proprietário: {self.proprietario.nome}"

  @app.route('/imoveis', methods=['POST', 'GET'])
  def handle_imoveis():
    if request.method == 'POST':
      if request.is_json:
        data = request.get_json()
        novo_imovel = Imovel(endereco=data['endereco'], cidade=data['cidade'], estado=data['estado'], cep=data['cep'], tipo_imovel=data['tipo_imovel'], descricao_imovel=data['descricao_imovel'], id_proprietario=data['id_proprietario'])
        db.session.add(novo_imovel)
        db.session.commit()
        return {'Mensagem': f"Imóvel {novo_imovel.id} foi criado com sucesso."}
      else:
        return {"Erro": "A requesição não foi carregada no formato JSON."}
    
    elif request.method == 'GET':
      imoveis = Imovel.query.all()
      results = [
        {          
          'endereco': imovel.endereco,
          'cidade': imovel.cidade,
          'estado': imovel.estado,
          'cep': imovel.cep,
          'tipo_imovel': imovel.tipo_imovel,
          'descricao_imovel': imovel.descricao_imovel,
          'id': imovel.id,
          'proprietario': {
            'nome': imovel.proprietario.nome,
            'cpf_cnpj': imovel.proprietario.cpf_cnpj,
            'id': imovel.proprietario.id
          }
        } for imovel in imoveis
      ]

      return {"Total de Imóveis": len(results), "Imóveis": results}

  @app.route('/imoveis/<imovel_id>', methods=['GET', 'PUT', 'DELETE'])
  def handle_imovel(imovel_id):
    imovel = Imovel.query.get_or_404(imovel_id)
    if request.method == 'GET':
      response = {         
          'endereco': imovel.endereco,
          'cidade': imovel.cidade,
          'estado': imovel.estado,
          'cep': imovel.cep,
          'tipo_imovel': imovel.tipo_imovel,
          'descricao_imovel': imovel.descricao_imovel,
          'id': imovel.id,
          'proprietario': {
          'nome': imovel.proprietario.nome,
          'cpf_cnpj': imovel.proprietario.cpf_cnpj,
          'id': imovel.proprietario.id
          }
      }
      return {"Mensagem": "Sucesso", "imóvel": response}
    
    elif request.method == 'PUT':
      data = request.get_json()      
      imovel.endereco = data['endereco']
      imovel.cidade=data['cidade']
      imovel.estado=data['estado']
      imovel.cep=data['cep']
      imovel.tipo_imovel=data['tipo_imovel']
      imovel.descricao_imovel=data['descricao_imovel']
      imovel.id_proprietario=data['id_proprietario']
      db.session.add(imovel)
      db.session.commit()
      return {"Mensagem": f"Imóvel {imovel.id} atualizado com sucesso!"}
    
    elif request.method == 'DELETE':
      db.session.delete(imovel)
      db.session.commit()
      return {"Mensagem": f"Imóvel {imovel.id} deletado com sucesso!"}


class Contrato(db.Model):
  __tablename__ = 'contratos'

  id = db.Column(db.Integer, primary_key=True)
  inicio_contrato = db.Column(db.String())
  termino_contrato = db.Column(db.String())
  valor = db.Column(db.String())
  id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False) 
  id_corretor = db.Column(db.Integer, db.ForeignKey('corretores.id'), nullable=False)
  id_imovel = db.Column(db.Integer, db.ForeignKey('imoveis.id'), nullable=False)

  def __init__(self, inicio_contrato, termino_contrato, valor, id_cliente, id_corretor, id_imovel):
    self.inicio_contrato = inicio_contrato
    self.termino_contrato = termino_contrato
    self.valor = valor
    self.id_cliente = id_cliente
    self.id_corretor = id_corretor
    self.id_imovel = id_imovel
  
  def __repr__(self):
    return f"<Campo Contrato\n.....>"

  @app.route('/contratos', methods=['POST', 'GET'])
  def handle_contratos():
    if request.method == 'POST':
      if request.is_json:
        data = request.get_json()
        novo_contrato = Contrato(inicio_contrato=data['inicio_contrato'], termino_contrato=data['termino_contrato'], valor=data['valor'], id_cliente=data['id_cliente'], id_corretor=data['id_corretor'], id_imovel=data['id_imovel'])
        db.session.add(novo_contrato)
        db.session.commit()
        return {'Mensagem': f"Contrato {novo_contrato.id} foi criado com sucesso."}
      else:
        return {"Erro": "A requesição não foi carregada no formato JSON."}
    
    elif request.method == 'GET':
      contratos = Contrato.query.all()
      results = [
        {          
          'inicio_contrato': contrato.inicio_contrato,
          'termino_contrato': contrato.termino_contrato,
          'valor': contrato.valor,
          'cliente': {
            'nome': contrato.cliente.nome
          },
          'corretor':{
            'nome': contrato.corretor.nome
          },
          'imovel':{
            'id': contrato.imovel.id,
            'proprietario': contrato.imovel.id_proprietario,
            'descricao': contrato.imovel.descricao_imovel
          },
          'id': contrato.id,
        } for contrato in contratos
      ]

      return {"Total de Contratos": len(results), "Contratos": results}

  @app.route('/contratos/<contrato_id>', methods=['GET', 'PUT', 'DELETE'])
  def handle_contrato(contrato_id):
    contrato = Contrato.query.get_or_404(contrato_id)
    if request.method == 'GET':
      response = {         
          'inicio_contrato': contrato.inicio_contrato,
          'termino_contrato': contrato.termino_contrato,
          'valor': contrato.valor,
          'cliente': {
            'nome': contrato.cliente.nome
          },
          'corretor':{
            'nome': contrato.corretor.nome
          },
          'imovel':{
            'id': contrato.imovel.id,
            'proprietario': contrato.imovel.id_proprietario,
            'descricao': contrato.imovel.descricao_imovel
          }
      }
      return {"Mensagem": "Sucesso", "Contratos": response}
    
    elif request.method == 'PUT':
      data = request.get_json()      
      contrato.inicio_contrato = data['inicio_contrato']
      contrato.cidade=data['termino_contrato']
      contrato.valor=data['valor']
      contrato.id_cliente=data['id_cliente']
      contrato.id_corretor=data['id_corretor']
      contrato.id_imovel=data['id_imovel']
      db.session.add(contrato)
      db.session.commit()
      return {"Mensagem": f"Contrato {contrato.id} atualizado com sucesso!"}
    
    elif request.method == 'DELETE':
      db.session.delete(contrato)
      db.session.commit()
      return {"Mensagem": f"Contrato {contrato.id} deletado com sucesso!"}

@login_manager.user_loader
def load_user(usuario_id):
  return Usuario.query.get(int(usuario_id))

#Rotas de Login
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    senha = request.form.get('senha')
    lembrar = True if request.form.get('lembrar') else False

    usuario = Usuario.query.filter_by(email=email).first()
    print(email)
    if not usuario or not check_password_hash(usuario.senha, senha):
        flash('Senha ou email incorretos!')
        return redirect(url_for('login'))
    login_user(usuario, remember=lembrar) 
    return redirect(url_for('menuNavegacao'))

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    nome = request.form.get('nome')
    senha = request.form.get('senha')

    usuario = Usuario.query.filter_by(email=email).first() 

    if usuario:
        flash('Email já cadastrado') 
        return redirect(url_for('signup'))
    novo_usuario = Usuario(email=email, nome=nome, senha=generate_password_hash(senha, method='sha256'))

    
    db.session.add(novo_usuario)
    db.session.commit()

    return redirect(url_for('login'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/menuNavegacao', methods=['POST', 'GET'])
@login_required
def menuNavegacao():
  return render_template('menuNavegacao.html')


##CONTRATO
@app.route('/contrato_menu', methods=['POST', 'GET'])
@login_required
def contrato_menu():
  return render_template('contrato/contrato_menu.html', contratos = Contrato.query.all())

@app.route('/contrato_cadastro', methods = ['GET', 'POST'])
@login_required
def contrato_cadastro():
  if request.method == 'POST':
    if not request.form['inicio_contrato'] or not request.form['termino_contrato'] or not request.form['valor'] or not request.form['id_cliente'] or not request.form['id_corretor'] or not request.form['id_imovel']:
      flash('Por favor, insira todos os campos', 'error')
    else:
      contrato = Contrato(
        inicio_contrato=request.form['inicio_contrato'],
        termino_contrato=request.form['termino_contrato'],
        valor=request.form['valor'],
        id_cliente=request.form['id_cliente'],
        id_corretor=request.form['id_corretor'],
        id_imovel=request.form['id_imovel']
      )
      db.session.add(contrato)
      db.session.commit()
      flash('Cadastro realizado!')
      return redirect(url_for('contrato_menu'))
  imoveis = Imovel.query.all()
  clientes = Cliente.query.all()
  corretores = Corretor.query.all()
  return render_template(
    'contrato/contrato_cadastro.html', 
    imoveis=imoveis, 
    clientes=clientes,
    corretores=corretores
  )

@app.route('/contrato_alterar/<contrato_id>', methods=['GET', 'POST'])
@login_required
def contrato_alterar(contrato_id):
  contrato = Contrato.query.get_or_404(contrato_id)
  if request.method == 'POST':    
      contrato.inicio_contrato = request.form['inicio_contrato']
      contrato.termino_contrato = request.form['termino_contrato']
      contrato.valor = request.form['valor']
      contrato.id_cliente=request.form['id_cliente']
      contrato.id_corretor=request.form['id_corretor']
      contrato.id_imovel=request.form['id_imovel']
      db.session.add(contrato)
      db.session.commit()
      flash('Atulização realizada!')
      return redirect(url_for('contrato_menu'))
  imoveis = Imovel.query.all()
  clientes = Cliente.query.all()
  corretores = Corretor.query.all()
  
  return render_template(
    'contrato/contrato_alterar.html', 
    imoveis=imoveis, 
    clientes=clientes,
    corretores=corretores,
    contrato=contrato
  )

@app.route('/contrato_visualizar/<contrato_id>', methods=['GET'])
@login_required
def contrato_visualizar(contrato_id):
  contrato = Contrato.query.get_or_404(contrato_id)          
  return render_template('contrato/contrato_visualizar.html', contrato = contrato)


@app.route('/contrato_menu/<contrato_id>/delete', methods=['GET','POST'])
@login_required
def contrato_delete(contrato_id):
  contrato = Contrato.query.get_or_404(contrato_id)
  if request.method == 'POST':
    if contrato:
      db.session.delete(contrato)
      db.session.commit()
      return redirect('/contrato_menu')
    abort(404)
  return render_template('/static/form.js', link_cancelar='contrato_menu')

##CLIENTE
@app.route('/cliente_menu', methods=['POST', 'GET'])
@login_required
def cliente_menu():
  return render_template('cliente/cliente_menu.html', clientes = Cliente.query.all())

@app.route('/cliente_cadastro', methods = ['GET', 'POST'])
@login_required
def cliente_cadastro():
  if request.method == 'POST':
    if not request.form['nome'] or not request.form['cpf_cnpj'] or not request.form['tipo_pessoa'] or not request.form['endereco'] or not request.form['cidade'] or not request.form['estado'] or not request.form['cep']or not request.form['telefone'] or not request.form['email']:
      flash('Por favor, insira todos os campos', 'error')
    else:
      cliente = Cliente(request.form['nome'], request.form['cpf_cnpj'],request.form['tipo_pessoa'], request.form['endereco'], request.form['cidade'],request.form['estado'], request.form['cep'], request.form['telefone'], request.form['email'])
      db.session.add(cliente)
      db.session.commit()
      flash('Cadastro realizado!')
      return redirect(url_for('cliente_menu'))
  return render_template('cliente/cliente_cadastro.html')

@app.route('/cliente_alterar/<cliente_id>', methods=['GET', 'POST'])
@login_required
def cliente_alterar(cliente_id):
  cliente = Cliente.query.get_or_404(cliente_id)
  if request.method == 'POST':    
      cliente.nome = request.form['nome']
      cliente.cpf_cnpj = request.form['cpf_cnpj']
      cliente.tipo_pessoa = request.form['tipo_pessoa']
      cliente.endereco = request.form['endereco']
      cliente.cidade = request.form['cidade']
      cliente.estado = request.form['estado']
      cliente.cep = request.form['cep']
      cliente.telefone=request.form['telefone']
      cliente.email=request.form['email']
      db.session.add(cliente)
      db.session.commit()
      flash('Atulização realizada!')
      return redirect(url_for('cliente_menu'))
  return render_template('cliente/cliente_alterar.html', cliente = cliente)

@app.route('/cliente_visualizar/<cliente_id>', methods=['GET'])
@login_required
def cliente_visualizar(cliente_id):
  cliente = Cliente.query.get_or_404(cliente_id)          
  return render_template('cliente/cliente_visualizar.html', cliente = cliente)

@app.route('/cliente_menu/<cliente_id>/delete', methods=['GET','POST'])
@login_required
def cliente_delete(cliente_id):
  cliente = Cliente.query.get_or_404(cliente_id)
  if request.method == 'POST':
    if cliente:
      db.session.delete(cliente)
      db.session.commit()
      return redirect('/cliente_menu')
    abort(404)
  return render_template('delete.html', link_cancelar='cliente_menu')



## IMOVEL
@app.route('/imovel_menu', methods=['POST', 'GET'])
@login_required
def imovel_menu():
  return render_template('imovel/imovel_menu.html', imoveis = Imovel.query.all())

@app.route('/imovel_cadastro', methods = ['GET', 'POST'])
@login_required
def imovel_cadastro():
  if request.method == 'POST':
    if not request.form['endereco'] or not request.form['cidade'] or not request.form['estado'] or not request.form['cep'] or not request.form['id_proprietario'] or not request.form['tipo_imovel'] or not request.form['descricao_imovel']:
      flash('Por favor, insira todos os campos', 'error')
    else:
      imovel = Imovel(
        endereco=request.form['endereco'],
        cidade=request.form['cidade'],
        estado=request.form['estado'],
        cep=request.form['cep'],
        id_proprietario=request.form['id_proprietario'],
        tipo_imovel=request.form['tipo_imovel'],
        descricao_imovel=request.form['descricao_imovel']
      )
      db.session.add(imovel)
      db.session.commit()
      flash('Cadastro realizado!')
      return redirect(url_for('imovel_menu'))
  proprietarios = Proprietario.query.all()
  return render_template('imovel/imovel_cadastro.html', proprietarios = proprietarios)

@app.route('/imovel_alterar/<imovel_id>', methods=['GET', 'POST'])
@login_required
def imovel_alterar(imovel_id):
  imovel = Imovel.query.get_or_404(imovel_id)
  if request.method == 'POST':    
      imovel.endereco = request.form['endereco']
      imovel.cidade = request.form['cidade']
      imovel.estado = request.form['estado']
      imovel.cep=request.form['cep']
      imovel.tipo_imovel=request.form['tipo_imovel']
      imovel.descricao_imovel=request.form['descricao_imovel']
      imovel.id_proprietario=request.form['id_proprietario']
      db.session.add(imovel)
      db.session.commit()
      flash('Atulização realizada!')
      return redirect(url_for('imovel_menu'))
  proprietarios = Proprietario.query.all()    
  return render_template('imovel/imovel_alterar.html',
   imovel = imovel,
   proprietarios = proprietarios)

@app.route('/imovel_visualizar/<imovel_id>', methods=['GET'])
@login_required
def imovel_visualizar(imovel_id):
  imovel = Imovel.query.get_or_404(imovel_id)          
  return render_template('imovel/imovel_visualizar.html', imovel = imovel)

@app.route('/imovel_menu/<imovel_id>/delete', methods=['GET','POST'])
@login_required
def imovel_delete(imovel_id):
  imovel = Imovel.query.get_or_404(imovel_id)
  if request.method == 'POST':
    if imovel:
      db.session.delete(imovel)
      db.session.commit()
      return redirect('/imovel_menu')
    abort(404)
  return render_template('delete.html', link_cancelar='imovel_menu')


##PROPRIETARIO
@app.route('/proprietario_menu', methods=['POST', 'GET'])
@login_required
def proprietario_menu():
  return render_template('proprietario/proprietario_menu.html', proprietarios = Proprietario.query.all())

@app.route('/proprietario_cadastro', methods = ['GET', 'POST'])
@login_required
def proprietario_cadastro():
  if request.method == 'POST':
    if not request.form['nome'] or not request.form['cpf_cnpj'] or not request.form['tipo_pessoa'] or not request.form['endereco'] or not request.form['cidade'] or not request.form['estado'] or not request.form['cep']or not request.form['telefone'] or not request.form['email']:
      flash('Por favor, insira todos os campos', 'error')
    else:
      proprietario = Proprietario(request.form['nome'], request.form['cpf_cnpj'],request.form['tipo_pessoa'], request.form['endereco'], request.form['cidade'],request.form['estado'], request.form['cep'], request.form['telefone'], request.form['email'])
      db.session.add(proprietario)
      db.session.commit()
      flash('Cadastro realizado!')
      return redirect(url_for('proprietario_menu'))
  return render_template('proprietario/proprietario_cadastro.html')

@app.route('/proprietario_alterar/<proprietario_id>', methods=['GET', 'POST'])
@login_required
def proprietario_alterar(proprietario_id):
  proprietario = Proprietario.query.get_or_404(proprietario_id)
  if request.method == 'POST':    
      proprietario.nome = request.form['nome']
      proprietario.cpf_cnpj = request.form['cpf_cnpj']
      proprietario.tipo_pessoa = request.form['tipo_pessoa']
      proprietario.endereco = request.form['endereco']
      proprietario.cidade = request.form['cidade']
      proprietario.estado = request.form['estado']
      proprietario.cep = request.form['cep']
      proprietario.telefone=request.form['telefone']
      proprietario.email=request.form['email']
      db.session.add(proprietario)
      db.session.commit()
      flash('Atulização realizada!')
      return redirect(url_for('proprietario_menu'))
  return render_template('proprietario/proprietario_alterar.html', proprietario = proprietario)

@app.route('/proprietario_visualizar/<proprietario_id>', methods=['GET'])
@login_required
def proprietario_visualizar(proprietario_id):
  proprietario = Proprietario.query.get_or_404(proprietario_id)          
  return render_template('proprietario/proprietario_visualizar.html', proprietario = proprietario)


@app.route('/proprietario_menu/<proprietario_id>/delete', methods=['GET','POST'])
@login_required
def proprietario_delete(proprietario_id):
  proprietario = Proprietario.query.get_or_404(proprietario_id)
  if request.method == 'POST':
    if proprietario:
      db.session.delete(proprietario)
      db.session.commit()
      return redirect('/proprietario_menu')
    abort(404)
  return render_template('delete.html', link_cancelar='proprietario_menu')





#CORRETOR
@app.route('/corretor_menu', methods=['POST', 'GET'])
@login_required
def corretor_menu():
  corretores = Corretor.query.order_by("id").all()
  return render_template('corretor/corretor_menu.html', corretores = corretores)

@app.route('/corretor_cadastro', methods = ['GET', 'POST'])
@login_required
def corretor_cadastro():
  if request.method == 'POST':
    if not request.form['nome'] or not request.form['cpf_cnpj'] or not request.form['tipo_pessoa'] or not request.form['telefone'] or not request.form['email']:
      flash('Por favor, insira todos os campos', 'error')
    else:
      corretor = Corretor(request.form['nome'], request.form['cpf_cnpj'],request.form['tipo_pessoa'], request.form['telefone'], request.form['email'])
      db.session.add(corretor)
      db.session.commit()
      flash('Cadastro realizado!')
      return redirect(url_for('corretor_menu'))
  return render_template('corretor/corretor_cadastro.html')

@app.route('/corretor_alterar/<corretor_id>', methods=['GET', 'POST'])
@login_required
def corretor_alterar(corretor_id):
  corretor = Corretor.query.get_or_404(corretor_id)
  if request.method == 'POST':    
      corretor.nome = request.form['nome']
      corretor.cpf_cnpj = request.form['cpf_cnpj']
      corretor.tipo_pessoa = request.form['tipo_pessoa']
      corretor.telefone=request.form['telefone']
      corretor.email=request.form['email']
      db.session.add(corretor)
      db.session.commit()
      flash('Atulização realizada!')
      return redirect(url_for('corretor_menu'))
  return render_template('corretor/corretor_alterar.html', corretor = corretor)

@app.route('/corretor_visualizar/<corretor_id>', methods=['GET'])
@login_required
def corretor_visualizar(corretor_id):
  corretor = Corretor.query.get_or_404(corretor_id)          
  return render_template('corretor/corretor_visualizar.html', corretor = corretor)  

@app.route('/corretor_menu/<corretor_id>/delete', methods=['POST'])
@login_required
def corretor_delete(corretor_id):
  corretor = Corretor.query.get_or_404(corretor_id)
  if request.method == 'POST':
    if corretor:
      db.session.delete(corretor)
      db.session.commit()
      flash("Registro deletado com sucesso!")
      return redirect('/corretor_menu')
    abort(404)
  return render_template('delete.html', link_cancelar='corretor_menu')




if __name__ == '__main__':
  app.run(debug=True)


