from transporte import Transporte

class Aereo(Transporte):
    def __init__(self,  lotacao, velocidade_max, comprimento, fabricante, proprietario, altitude_max, n_trem_de_pouso, comprimento_cauda):
        super().__init__(lotacao, velocidade_max, comprimento, fabricante, proprietario)
        self.altitude_max = altitude_max
        self.n_trem_de_pouso = n_trem_de_pouso
        self.comprimento_cauda = comprimento_cauda
        
class Aviao(Aereo):
    def __init__(self, lotacao, velocidade_max, comprimento, fabricante, proprietario, altitude_max, n_trem_de_pouso, comprimento_cauda, n_flaps, finalidade_aeronave, tipo_turbina):
        super().__init__(lotacao, velocidade_max, comprimento, fabricante, proprietario, altitude_max, n_trem_de_pouso, comprimento_cauda)
        self.n_flaps = n_flaps
        self.finalidade_aeronave = finalidade_aeronave
        self.tipo_turbina = tipo_turbina

class Helicoptero(Aereo):
    def __init__(self,lotacao, velocidade_max, comprimento, fabricante, proprietario, altitude_max, n_trem_de_pouso, comprimento_cauda, potencia_rotor, qtde_rotores,):
        super().__init__(lotacao, velocidade_max, comprimento, fabricante, proprietario, altitude_max, n_trem_de_pouso, comprimento_cauda)
        self.potencia_rotor = potencia_rotor
        self.qtde_rotores = qtde_rotores

# Exemplos de Uso das Classes Avião e Helicoptero

boing = Aviao("300 pessoas", "10.000Km/h", "76 metros", "Embraer", "Joaozinho Cia", "11.000 metros", "4","60 metros", "4", "comercial/intercontinental","Gás")
print("Caracteristicas do Boing")
print(f"Lotação: {boing.lotacao}, Velocidade Máxima: {boing.velocidade_max}, Comprimento: {boing.comprimento}, Fabricante: {boing.fabricante}, Proprietário: {boing.proprietario}, Altitude Máxima: {boing.altitude_max}, Nº de Trem de Pouso: {boing.n_trem_de_pouso}, Comprimento da Cauda: {boing.comprimento_cauda}, Nº de Flaps: {boing.n_flaps}, Finalidade: {boing.finalidade_aeronave}, Tipo de Turbina: {boing.tipo_turbina}")

print()

bell = Helicoptero("6 pessoas", "289km/h","11 metros","Airbus Helicopters","Joaozinho Helicopters","6.000 metros", "2", "6 metros", "600","2" )
print("Caracteristicas do Helicoptero Bell")
print(f"Lotação: {bell.lotacao}, Velocidade Máxima: {bell.velocidade_max}, Comprimento: {bell.comprimento}, Fabricante: {bell.fabricante}, Proprietário: {bell.proprietario}, Altitude Máxima: {bell.altitude_max}, Nº de Trem de Pouso: {bell.n_trem_de_pouso}, Comprimento da Cauda: {bell.comprimento_cauda}, Potencia do Rotor: {bell.potencia_rotor}, Quantidade de Rotores: {bell.qtde_rotores}")