from imoveis import Imoveis
from function_cadastroPessoa import opcao2, proprietarios


def cadastro():
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
      opcao01()
      
    elif opcao == 2: #Verificar Lista de Imóveis   
      opcao02()
    elif opcao == 0:#Sair
      opcao00()
      return True    
  else:
    print("Opção Inválida!")
    return False

def opcao01():  #Cadastrar Novo Imóvel
  print("---------------------------") 
  print("Preencha os campos abaixo:")
  print("---------NOVO IMÓVEL-------")  
  endereco = str(input("Rua/Nº/Bairro/Cidade/UF: "))
  proprietario = busca_proprietario()
  tipo_de_imovel = str(input("Residencial ou Comercial: "))
  descricao_imovel = str(input("Descreva o imóvel:"))
  valor_mensal = str(input("Valor Mensal: R$"))
  novo_imovel = Imoveis(endereco, proprietario, tipo_de_imovel, descricao_imovel,valor_mensal)
  imovel.append(novo_imovel)
  print()
  print("IMÓVEIS CADASTRADOS")
  print(novo_imovel)

def opcao02(): #Verificar Lista de Imóveis
  if len(imovel) <= 0:
    print("Nenhum Imóvel cadastrado")
  else:
    print("----LISTA DE IMÓVEIS----")
    for item in imovel:
      print(item)
      print()

def opcao00(): #Sair
  print("Encerrando....")

def busca_proprietario():  
  doc_identificacao = str(input("CPF/CNPJ: "))
  if len(proprietarios) <= 0:
    novoProprietario = opcao2()
  else:   
    for proprietario in proprietarios:
      if proprietario.doc_identificacao == doc_identificacao:
        novoProprietario = proprietario
        break       
    if not novoProprietario:        
      novoProprietario = opcao2()
      
  print("Proprietário vinculado ao imóvel.")
  return novoProprietario 
        
      


imovel = list()
print("-"*22)
print("  PAINEL DE CADASTRO  ")
cadastro()
