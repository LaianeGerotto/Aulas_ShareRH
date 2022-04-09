from functions import menuAnterior
from function_menuCliente import busca_cliente
from function_menuCorretor import busca_corretor, escolhaCorretor
from contratos import Contrato
from function_menuImoveis import busca_imoveis



def menuContratos():
  while True:
    print("Escolha uma das opções abaixo:")
    print("1 - Novo Contrato")
    print("2 - Lista de Contratos Ativos")
    print("3 - Deletar Contrato")
    print("0 - Retornar ao Menu anterior/Encerrar")
    opcao = int(input("Opção: "))
    if escolhaContratos(opcao):
        break


def escolhaContratos(opcao):    
  if opcao in [1,2,3,0]:    
    if opcao == 1: #Cadastrar novo contrato
      novoContrato()
      
    elif opcao == 2: #Lista de Contratos   
      listaContratos()

    elif opcao == 3: #Deletar Cliente
      deletarContratos()                  
        
    elif opcao == 0:#Sair
      menuAnterior()
      return True    
  else:
    print("Opção Inválida!")
    return False


def novoContrato():
  print("-----------------------------")   
  print("---------NOVO CONTRATO-------")
  print("Preencha os campos abaixo:")
  num_contrato = str(input("Número do Contrato: "))
  corretor = busca_corretor()
  cliente = busca_cliente()
  imovel = busca_imoveis()
  inicio_contrato = str(input("Início Contrato: "))
  termino_contrato = str(input("Término Contrato: ")) 
  novo_contrato = Contrato(num_contrato,corretor, cliente, imovel, inicio_contrato, termino_contrato)
  contratos.append(novo_contrato)
  print()
  print()
  print(novo_contrato)
  return novo_contrato

def listaContratos():
  if len(contratos) <= 0:
      print("Nenhum contrato cadastrado!")
  else:
    print("-------------------------------")
    print("      LISTA DE CONTRATOS       ")
    print("-------------------------------")
    for item in contratos:
      print(item)
      print()

def deletarContratos():
  contratoDel = False
  print("-- Para DELETAR CONTRATO, preencha os dados abaixo: --")  
  num_contrato = str(input("Número do Contrato: "))
  if len(contratos) <= 0:
    print("Contrato não localizado!")
  else:   
    for contrato in contratos:
      if contrato.num_contrato == num_contrato:
        contratos.remove(contrato)
        print("Contrato excluído!")
        contratoDel = True
        break
  if contratoDel == False:      
    print("Contrato não localizado!")

contratos = list()

