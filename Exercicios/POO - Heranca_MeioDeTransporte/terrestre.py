from transporte import Transporte

class Terrestre(Transporte):
    def __init__(self, lotacao, velocidade_max, comprimento, fabricante, proprietario, n_de_rodas, n_de_marcha, n_de_chassi, placa, qtde_eixo):
        super().__init__(lotacao, velocidade_max, comprimento, fabricante, proprietario)
        self.n_de_rodas = n_de_rodas
        self.n_de_marcha = n_de_marcha
        self.n_de_chassi = n_de_chassi
        self.placa = placa
        self.qtde_eixo = qtde_eixo

class Carro(Terrestre):
    def __init__(self, lotacao, velocidade_max, comprimento, fabricante, proprietario, n_de_rodas, n_de_marcha, n_de_chassi, placa, qtde_eixo, capacidade_portaMala, tipo_combustivel):
        super().__init__(lotacao, velocidade_max, comprimento, fabricante, proprietario, n_de_rodas, n_de_marcha, n_de_chassi, placa, qtde_eixo)
        self.capacidade_portaMala = capacidade_portaMala
        self.tipo_combustivel = tipo_combustivel
        
class Caminhao(Terrestre):
    def __init__(self, lotacao, velocidade_max, comprimento, fabricante, proprietario, n_de_rodas, n_de_marcha, n_de_chassi, placa, qtde_eixo, tipo_carroceria, tipo_carga):
        super().__init__(lotacao, velocidade_max, comprimento, fabricante, proprietario, n_de_rodas, n_de_marcha, n_de_chassi, placa, qtde_eixo)
        self.tipo_carroceria = tipo_carroceria
        self.tipo_carga = tipo_carga

# Exemplos de Uso das Classes Carro e Caminhao

fusca = Carro("5","180km","2 metros","Volkswagen","Joaozinho", "4","5","00000000000","AAA000","0","200litros","gasolina")
print("Caracteristicas do Fusca")
print(f"Lotação: {fusca.lotacao}, Velocidade Máxima: {fusca.velocidade_max}, Comprimento: {fusca.comprimento}, Fabricante: {fusca.fabricante}, Proprietário: {fusca.proprietario}, Nº de Rodas: {fusca.n_de_rodas}, Nº de Marchas: {fusca.n_de_marcha},\nChassi: {fusca.n_de_chassi}, Placa: {fusca.placa}, Qtde de Eixos: {fusca.qtde_eixo}, Capacidade Porta-Mala: {fusca.capacidade_portaMala}, Tipo de Combustivel: {fusca.tipo_combustivel}")

print()

volvo = Caminhao("3","200","3 metros","Volvo", "Joaozinho","12","16","0000000111","BBB111","1","Baú","Grãos")
print("Caracteristicas do Caminhão Volvo")
print(f"Lotação: {volvo.lotacao}, Velocidade Máxima: {volvo.velocidade_max}, Comprimento: {volvo.comprimento}, Fabricante: {volvo.fabricante}, Proprietário: {volvo.proprietario}, Nº de Rodas: {volvo.n_de_rodas}, Nº de Marchas: {volvo.n_de_marcha},\nChassi: {volvo.n_de_chassi}, Placa: {volvo.placa}, Qtde de Eixos: {volvo.qtde_eixo}, Tipo de Carroceria: {volvo.tipo_carroceria}, Tipo de Carga: {volvo.tipo_carga}")