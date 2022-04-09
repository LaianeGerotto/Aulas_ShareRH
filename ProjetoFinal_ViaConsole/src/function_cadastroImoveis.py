from imoveis import Imoveis
from function_cadastroPessoa import cadastroProprietario, proprietarios, busca_proprietario
from function_login import encerrarSistema

def menuImoveis():
  while True:
    print()
    print("Escolha uma das opções abaixo:")
    print("1 - Cadastrar NOVO IMÓVEL")
    print("2 - Verificar Lista de Imóveis")
    print("0 - Encerrar")
    opcao = int(input("Opção: "))
    if escolha(opcao):
        break
    
def escolha(opcao):    
  if opcao in [1,2,0]:    
    if opcao == 1: #Cadastrar Novo Imóvel
      cadastroImovel()
      
    elif opcao == 2: #Verificar Lista de Imóveis   
      listaImoveis()
    elif opcao == 0:#Sair
      encerrarSistema()
      return True    
  else:
    print("Opção Inválida!")
    return False

def cadastroImovel():  #Cadastrar Novo Imóvel
  print("---------------------------") 
  print("Preencha os campos abaixo:")
  print("---------NOVO IMÓVEL-------")
  cod_imovel = str(input("Código Imóvel: "))  
  endereco = str(input("Rua/Nº/Bairro/Cidade/UF: "))
  proprietario = busca_proprietario()
  tipo_de_imovel = str(input("Residencial ou Comercial: "))
  descricao_imovel = str(input("Descreva o imóvel:"))
  valor_mensal = str(input("Valor Mensal: R$"))
  novo_imovel = Imoveis(cod_imovel,endereco, proprietario, tipo_de_imovel, descricao_imovel,valor_mensal)
  imoveis.append(novo_imovel)
  print()
  print("IMÓVEIS CADASTRADOS")
  print(novo_imovel)

def listaImoveis(): #Verificar Lista de Imóveis
  if len(imoveis) <= 0:
    print("Nenhum Imóvel cadastrado")
  else:
    print("----LISTA DE IMÓVEIS----")
    for item in imoveis:
      print(item)
      print()

# def opcao00(): #Sair
#   print("Encerrando....")
     
def busca_imoveis():
  novoImovel = None  
  cod_imovel = str(input("Código Imóvel: "))
  if len(imoveis) <= 0:
    novoImovel = cadastroImovel()
  else:   
    for imovel in imoveis:
      if imovel.cod_imovel == cod_imovel:
        novoImovel = imovel
        break       
    if not novoImovel:        
      novoImovel = cadastroImovel()
      
  print("Imóvel vinculado.")
  print(novoImovel)
  return novoImovel        

imoveis = list()
print("-"*22)
print("  PAINEL DE CADASTRO  ")
#cadastro()
