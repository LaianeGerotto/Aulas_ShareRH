from pessoa import Proprietario
from functions import menuAnterior

def cadastroProprietario():  #Cadastrar PROPRIETÁRIO
  print("Preencha os campos abaixo:")
  print("CAMPO PROPRIETÁRIO")
  nome = str(input("Nome/Razão Social: ")).upper()
  tipo_pessoa = str(input("Pessoa Fisica ou Juridica: "))
  doc_identificacao = str(input("CPF/CNPJ: "))
  data = str(input("Data de Nascimento ou Fundação: "))
  endereco = str(input("Rua/Nº/Bairro/Cidade/UF: ")) 
  telefone = str(input("DDD+Telefone: "))
  email = str(input("Email: "))
  novo_proprietario = Proprietario(nome, tipo_pessoa, doc_identificacao, data, endereco, telefone, email)
  proprietarios.append(novo_proprietario)
  print("***** DADOS CADASTRADOS *****")
  print()
  print(novo_proprietario)
  return novo_proprietario

def listaProprietario(): #Verificar Lista de Proprietários
  if len(proprietarios) <= 0:
    print("Nenhum proprietário cadastrado")
  else:
    print("-------------------------------")
    print("     LISTA DE PROPRIETÁRIO     ")
    print("-------------------------------")
    for proprietario in proprietarios:
      print(proprietario)
      print()

def busca_proprietario():
  novoProprietario = None
  print("-- DADOS PROPRIETÁRIO --")  
  doc_identificacao = str(input("CPF/CNPJ: "))
  if len(proprietarios) <= 0:
    novoProprietario = cadastroProprietario()
  else:   
    for proprietario in proprietarios:
      if proprietario.doc_identificacao == doc_identificacao:
        novoProprietario = proprietario
        break       
    if not novoProprietario:        
      novoProprietario = cadastroProprietario()
      
  print("Proprietário vinculado!")
  return novoProprietario 

def escolhaProprietario(opcao1):    
  if opcao1 in [1,2,3,0]:    
    if opcao1 == 1: #Cadastro Proprietário
      cadastroProprietario()
      
    elif opcao1 == 2: #Lista de Proprietários    
      listaProprietario()
        
    elif opcao1 == 3: #Deletar Proprietário
      deletarProprietario()

    elif opcao1 == 0:#Sair
      menuAnterior()
      return True
    
  else:
    print("Opção Inválida!")
    return False

def deletarProprietario():
  proprietarioDel = False
  print("-- Para DELETAR PROPRIETÁRIO, preencha os dados abaixo: --")    
  doc_identificacao = str(input("CPF/CNPJ: "))
  if len(proprietarios) <= 0:
    print("Proprietário não localizado!")
  else:   
    for proprietario in proprietarios:
      if proprietario.doc_identificacao == doc_identificacao:
        proprietarios.remove(proprietario)
        print("Proprietário excluído!")
        proprietarioDel = True
        break
    if proprietarioDel == False:        
      print("Proprietário não localizado!")

proprietarios = list()

        