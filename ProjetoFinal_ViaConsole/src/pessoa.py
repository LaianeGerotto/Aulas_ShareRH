class Pessoa():
  def __init__(self, nome, tipo_pessoa, doc_identificacao, data, endereco, telefone, email):
    self.nome = nome
    self.tipo_pessoa = tipo_pessoa
    self.doc_identificacao = doc_identificacao
    self.data = data
    self.endereco = endereco
    self.telefone = telefone
    self.email = email

class Cliente(Pessoa):
  def __init__(self, nome, tipo_pessoa, doc_identificacao, data, endereco, telefone, email):
      super().__init__(nome, tipo_pessoa, doc_identificacao, data, endereco, telefone, email)
      
  
  def __repr__(self):
    return f"Nome: {self.nome}\nFisica/Juridica: {self.tipo_pessoa}\nCPF/CNPJ: {self.doc_identificacao}\nData de Nasc/Fundação: {self.data}\nEndereço:{self.endereco}\nTelefone: {self.telefone}\nEmail: {self.email}"


class Corretor(Pessoa):
  def __init__(self, nome, tipo_pessoa, doc_identificacao, data, endereco, telefone, email, cadastro_imobiliario, validade_creci):
      super().__init__(nome, tipo_pessoa, doc_identificacao, data, endereco, telefone, email)
      self.cadastro_imobiliario = cadastro_imobiliario
      self.validade_creci = validade_creci
  
  def __repr__(self):
    return f"Nome: {self.nome}\nFisica/Juridica: {self.tipo_pessoa}\nCPF/CNPJ: {self.doc_identificacao}\nData de Nasc/Fundação: {self.data}\nEndereço:{self.endereco}\nTelefone: {self.telefone}\nEmail: {self.email}\nCRECI: {self.cadastro_imobiliario}\nValidade CRECI: {self.validade_creci}"


class Proprietario(Pessoa):
  def __init__(self, nome, tipo_pessoa, doc_identificacao, data, endereco, telefone, email): 
      super().__init__(nome, tipo_pessoa, doc_identificacao, data, endereco, telefone, email)
  
  def __repr__(self):
    return f"Nome: {self.nome}\nFisica/Juridica: {self.tipo_pessoa}\nCPF/CNPJ: {self.doc_identificacao}\nData de Nasc/Fundação: {self.data}\nEndereço:{self.endereco}\nTelefone: {self.telefone}\nEmail: {self.email}"


