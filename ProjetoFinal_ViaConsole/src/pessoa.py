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
  def __init__(self, nome, tipo_pessoa, doc_identificacao, data, endereco, telefone, email): #nome_fiador, doc_identificacao_fiador, data_fiador, endereco_fiador, telefone_fiador, email_fiador):
      super().__init__(nome, tipo_pessoa, doc_identificacao, data, endereco, telefone, email)
      #self.nome_fiador = nome_fiador
      #self.doc_identificacao_fiador = doc_identificacao_fiador
      #self.data_fiador = data_fiador
      #self.endereco_fiador = endereco_fiador
      #self.telefone_fiador = telefone_fiador
      #self.email_fiador = email_fiador
  
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
  def __init__(self, nome, tipo_pessoa, doc_identificacao, data, endereco, telefone, email): # cadastro_imoveis):
      super().__init__(nome, tipo_pessoa, doc_identificacao, data, endereco, telefone, email)
      #self.cadastro_imoveis = cadastro_imoveis
  
  def __repr__(self):
    return f"Nome: {self.nome}\nFisica/Juridica: {self.tipo_pessoa}\nCPF/CNPJ: {self.doc_identificacao}\nData de Nasc/Fundação: {self.data}\nEndereço:{self.endereco}\nTelefone: {self.telefone}\nEmail: {self.email}"


