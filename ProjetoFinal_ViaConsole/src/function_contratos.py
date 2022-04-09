from function_login import encerrarSistema
from function_cadastroPessoa import  busca_proprietario, busca_cliente, busca_corretor
from contratos import Contrato
from imoveis import Imoveis
from function_cadastroImoveis import busca_imoveis

from seed import cria_registros

def menuContratos():
  while True:
    print("Escolha uma das opções abaixo:")
    print("1 - Novo Contrato")
    print("2 - Lista de Contratos Ativos")
    print("0 - Encerrar")
    opcao = int(input("Opção: "))
    if escolha(opcao):
        break


def escolha(opcao):    
  if opcao in [1,2,0]:    
    if opcao == 1: #Cadastrar novo contrato
      novoContrato()
      
    elif opcao == 2: #Lista de Contratos   
      listaContratos()                  
        
    elif opcao == 0:#Sair
      encerrarSistema()
      return True    
  else:
    print("Opção Inválida!")
    return False


def novoContrato():
  print("---------------------------")   
  print("---------NOVO CONTRATO-------")
  print("Preencha os campos abaixo:")
  corretor = busca_corretor()
  cliente = busca_cliente()
  imovel = busca_imoveis()
  inicio_contrato = str(input("Início Contrato: "))
  termino_contrato = str(input("Término Contrato: ")) 
  novo_contrato = Contrato(corretor, cliente, imovel, inicio_contrato, termino_contrato)
  contratos.append(novo_contrato)
  print()
  print("CONTRATO CADASTRADOS")
  print(novo_contrato)

def listaContratos():
  if len(contratos) <= 0:
      print("Nenhum contrato cadastrado")
  else:
    print("----LISTA DE CONTRATOS----")
    for item in contratos:
      print(item)
      print()


print("--  GESTÃO DE CONTRATOS --")
contratos = list()
cria_registros()
#cadastro()