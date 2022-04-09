from imoveis import Imoveis
from function_menuProprietario import cadastroProprietario, proprietarios, busca_proprietario

from functions import menuAnterior

def menuImoveis():
  while True:
    print()
    print("Escolha uma das opções abaixo:")
    print("1 - Cadastrar NOVO IMÓVEL")
    print("2 - Verificar Lista de Imóveis")
    print("3 - Deletar Imóvel")
    print("0 - Retornar ao Menu anterior/Encerrar")
    opcao = int(input("Opção: "))
    if escolhaImovel(opcao):
        break
    
def escolhaImovel(opcao):    
  if opcao in [1,2,3,0]:    
    if opcao == 1: #Cadastrar Novo Imóvel
      cadastroImovel()
      
    elif opcao == 2: #Verificar Lista de Imóveis   
      listaImoveis()

    elif opcao == 3: #Deletar Imóvel
      deletarImovel()
    
    elif opcao == 0:# Retornar
      menuAnterior()
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
  print("***** IMÓVEIS CADASTRADOS *****")
  print(novo_imovel)
  return novo_imovel

def listaImoveis(): #Verificar Lista de Imóveis
  if len(imoveis) <= 0:
    print("Nenhum Imóvel cadastrado")
  else:
    print("-------------------------------")
    print("       LISTA DE IMÓVEIS        ")
    print("-------------------------------")
    for item in imoveis:
      print(item)
      print()

     
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


def deletarImovel():
  imovelDel = False
  print("-- Para DELETAR CORRETOR, preencha os dados abaixo: --")  
  cod_imovel = str(input("Código do Imóvel: "))
  if len(imoveis) <= 0:
    print("Imóvel não localizado!")
  else:   
    for imovel in imoveis:
      if imovel.cod_imovel == cod_imovel:
        imoveis.remove(imovel)
        print("Imóvel excluído!")
        imovelDel = True
        break
    if imovelDel == False:        
      print("Imóvel não localizado!")

imoveis = list()

