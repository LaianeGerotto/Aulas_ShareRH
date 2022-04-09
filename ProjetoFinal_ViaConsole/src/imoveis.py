class Imoveis():
  def __init__(self, endereco, proprietario, tipo_de_imovel, descricao_imovel, valor_mensal):
    self.endereco = endereco
    self.proprietario = proprietario
    self.tipo_de_imovel = tipo_de_imovel
    self.descricao_imovel = descricao_imovel
    self.valor_mensal = valor_mensal

  def __repr__(self):
    return f"Endereço: {self.endereco}\nProprietário: {self.proprietario.nome}\nTipo do Imóvel: {self.tipo_de_imovel}\nDescrição do Imóvel: {self.descricao_imovel}\nValor Mensal: {self.valor_mensal}"