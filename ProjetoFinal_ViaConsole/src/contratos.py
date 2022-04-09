class Contrato():
  def __init__(self, num_contrato,corretor, cliente, imovel, inicio_contrato, termino_contrato):
    self.num_contrato = num_contrato    
    self.corretor = corretor
    self.cliente = cliente
    self.imovel = imovel
    self.inicio_contrato = inicio_contrato
    self.termino_contrato = termino_contrato

  def __repr__(self):
    return f"****** CONTRATO DE LOCAÇÃO ******\nNúmero do Contrato: {self.num_contrato}\nInicío de Contrato: {self.inicio_contrato}\nTérmino de Contrato: {self.termino_contrato}\nCorretor Responsável: {self.corretor.nome}\nCliente: {self.cliente.nome}\nProprietário: {self.imovel.proprietario.nome}\nCódigo do Imóvel: {self.imovel.cod_imovel}\n********************************"