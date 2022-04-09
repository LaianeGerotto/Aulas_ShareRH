from pessoa import Cliente, Proprietario, Corretor
from imoveis import Imoveis
from function_menuProprietario import proprietarios
from function_menuCliente import clientes
from function_menuCorretor import corretores
from function_menuImoveis import imoveis
from usuario import Usuario
from function_login import usuarios

def cria_registros():
  usuario1 = Usuario("teste", "teste@teste", "teste")

  proprietario1 = Proprietario("Meg Cristina", "Fisica","123456","10/07/2014","Rua Vira Lata Caramelo, nº 10 - Bairro: LadyDog, Cidade: Doguinho - Dogs/BR", "1111","meg@gmail.com")
  proprietario2 = Proprietario("Chokito Roberto", "Fisica","987654","01/07/2000","Rua Basset, nº 01 - Bairro: Canino, Cidade: Doguinho - Dogs/BR", "2222","chokito@gmail.com")

  imovel1 = Imoveis("0001", "Rua Carrocinha, nº 10 - Bairro: LadyDog, Cidade: Doguinho - Dogs/BR", proprietario1, "Residencial", "2 quartos, 1 Banheiro","1000,00")
  imovel2 = Imoveis("0002", "Rua Carrocinha, nº 10 - Bairro: LadyDog, Cidade: Doguinho - Dogs/BR", proprietario2, "Residencial", "1 quartos, 1 Banheiro","800,00")
  
  cliente1 = Cliente("Amora Maria", "Fisica", "101010","28/11/2017", "Rua Shitzu, nº 100 - Bairro: Fofinha, Cidade: Doguinho - Dogs/BR", "3333", "amora@gmail.com")
  cliente2 = Cliente("Ollaf José", "Fisica", "111012","28/11/2017", "Rua Shitzu Branco, nº 500 - Bairro: Fofinha, Cidade: Doguinho - Dogs/BR", "4444", "olaff@gmail.com")
  
  corretor1 = Corretor("Akira Maria", "Fisica", "010201","10/01/2000", "Rua Dos Husky, nº 11 - Bairro: LoboDog, Cidade: Doguinho - Dogs/BR","00000","akira@gmail.com","HK10011","31/12/2022")

  proprietarios.append(proprietario1)
  proprietarios.append(proprietario2)
  clientes.append(cliente1)
  clientes.append(cliente2)
  corretores.append(corretor1)
  imoveis.append(imovel1)
  imoveis.append(imovel2)
  usuarios.append(usuario1)