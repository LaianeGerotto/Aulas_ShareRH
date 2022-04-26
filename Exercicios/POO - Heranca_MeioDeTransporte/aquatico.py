from transporte import Transporte

class Aquatico(Transporte):
    def __init__(self, lotacao, velocidade_max, comprimento, fabricante, proprietario, profundidade):
        super().__init__(lotacao, velocidade_max, comprimento, fabricante, proprietario)
        self.profundidade = profundidade

class Remo(Aquatico):
    def __init__(self, lotacao, velocidade_max, comprimento, fabricante, proprietario, profundidade, qtde_pas):
        super().__init__(lotacao, velocidade_max, comprimento, fabricante, proprietario, profundidade)
        self.qtde_pas = qtde_pas
        
class Barco(Aquatico):
    def __init__(self, lotacao, velocidade_max, comprimento, fabricante, proprietario, profundidade, peso_ancora, altura_mastro):
        super().__init__(lotacao, velocidade_max, comprimento, fabricante, proprietario, profundidade)
        self.peso_ancora = peso_ancora
        self.altura_mastro = altura_mastro
        
# Exemplos de Uso das Classes Remo e Barco

skiff = Remo("1 pessoa", "20km/h","6 metros","Remos Skiff", "Joazinho", "50cm", "2" )
print("Caracteristicas do Remo Skiff")
print(f"Lotação: {skiff.lotacao}, Velocidade máxima: {skiff.velocidade_max}, Comprimento: {skiff.comprimento}, Fabricante: {skiff.fabricante}, Proprietário: {skiff.proprietario}, Profundidade: {skiff.profundidade}, Quantidade de Pás:{skiff.qtde_pas}")

print()
print("Caracteristicas do Iate")
iate = Barco("10 pessoas", "200km/h","12 metros","Joazinho Barcos", "Joazinho", "2 metros", "200kg", "7 metros")
print(f"Lotação: {iate.lotacao}, Velocidade máxima: {iate.velocidade_max}, Comprimento: {iate.comprimento}, Fabricante: {iate.fabricante}, Proprietário: {iate.proprietario}, Profundidade: {iate.profundidade}, Peso da âncora: {iate.peso_ancora}, Altura do Mastro: {iate.altura_mastro}")