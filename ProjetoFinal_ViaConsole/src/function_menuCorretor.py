from pessoa import Corretor
from functions import menuAnterior

def cadastroCorretor():  #Cadastrar Corretor
  print("---------------------------")   
  print("---------NOVO CORRETOR-------")
  nome = str(input("Nome/Razão Social: ")).upper()
  tipo_pessoa = str(input("Pessoa Fisica ou Juridica: "))
  doc_identificacao = str(input("CPF/CNPJ: "))
  data = str(input("Data de Nascimento ou Fundação:  "))
  endereco = str(input("Rua/Nº/Bairro/Cidade/UF:")) 
  telefone = str(input("DDD+Telefone: "))
  email = str(input("Email: "))
  cadastro_imobiliario = str(input("CRECI: "))
  validade_creci = str(input("Validade CRECI: "))
  novo_corretor = Corretor(nome, tipo_pessoa, doc_identificacao,data, endereco,telefone, email, cadastro_imobiliario, validade_creci)
  corretores.append(novo_corretor)
  print("***** DADOS CADASTRADOS *****")
  print()
  print(novo_corretor)  
  return novo_corretor

def listaCorretor(): #Verificar Lista de Corretores
  if len(corretores) <= 0:
    print("Nenhum corretor cadastrado")
  else:
    print("-------------------------------")
    print("      LISTA DE CORRETORES      ")
    print("-------------------------------")
    for corretor in corretores:
      print(corretor)
      print()

def busca_corretor():
  novoCorretor = None
  print("-- DADOS CORRETOR --")   
  doc_identificacao = str(input("CPF/CNPJ: "))
  if len(corretores) <= 0:
    novoCorretor = cadastroCorretor()
  else:   
    for corretor in corretores:
      if corretor.doc_identificacao == doc_identificacao:
        novoCorretor = corretor
        break       
    if not novoCorretor:        
      novoCorretor = cadastroCorretor()
      
  print("Corretor vinculado!")
  return novoCorretor  

def escolhaCorretor(opcao1):    
  if opcao1 in [1,2,3,0]:    
    if opcao1 == 1: #Cadastro Corretor
      cadastroCorretor()
      
    elif opcao1 == 2: #Lista de Corretores   
      listaCorretor()
        
    elif opcao1 == 3: #Deletar Cliente
      deletarCorretor()

    elif opcao1 == 0:#Sair
      menuAnterior()
      return True
    
  else:
    print("Opção Inválida!")
    return False

def deletarCorretor():
  corretorDel = False
  print("-- Para DELETAR CORRETOR, preencha os dados abaixo: --")  
  doc_identificacao = str(input("CPF/CNPJ: "))
  if len(corretores) <= 0:
    print("Corretor não localizado!")
  else:   
    for corretor in corretores:
      if corretor.doc_identificacao == doc_identificacao:
        corretores.remove(corretor)
        print("Corretor excluído!")
        corretorDel = True
        break
    if corretorDel == False:        
      print("Corretor não localizado!")

corretores = list()