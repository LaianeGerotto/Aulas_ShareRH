from pessoa import Cliente, Proprietario, Corretor
from function_login import encerrarSistema

print("PAINEL DE CADASTRO")

def menuPessoas():
  while True:
    print("Escolha uma das opções abaixo:")
    print("1 - Cadastrar CLIENTE/INQUILINO")
    print("2 - Cadastrar PROPRIETÁRIO")
    print("3 - Cadastrar CORRETOR")
    print("0 - Encerrar")
    opcao = int(input("Opção: "))
    if escolha(opcao):
        break

def escolha(opcao):    
  if opcao in [1,2,3,0]:    
    if opcao == 1: #Cadastrar CLIENTE/INQUILINO
      cadastroCliente()
      
    elif opcao == 2: #Cadastrar PROPRIETÁRIO    
      cadastroProprietario()      

    elif opcao == 3: #Cadastrar CORRETOR  
      cadastroCorretor()                   
        
    elif opcao == 0:#Sair
      encerrarSistema()
      return True    
  else:
    print("Opção Inválida!")
    return False

def cadastroCliente():  #Cadastrar CLIENTE/INQUILINO
  print("Preencha os campos abaixo:")
  print("CAMPO CLIENTE")
  nome = str(input("Nome/Razão Social: ")).upper()
  tipo_pessoa = str(input("Pessoa Fisica ou Juridica: "))
  doc_identificacao = str(input("CPF/CNPJ: "))
  data = str(input("Data de Nascimento ou Fundação: "))
  endereco = str(input("Rua/Nº/Bairro/Cidade/UF: ")) 
  telefone = str(input("DDD+Telefone: "))
  email = str(input("Email: ")) 
  novo_cliente = Cliente(nome, tipo_pessoa, doc_identificacao, data, endereco, telefone, email)
  clientes.append(novo_cliente)
  print("DADOS CADASTRADOS")
  print()
  print(novo_cliente)

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
  #cadastro_imoveis (inserir a função de Imoveis)
  novo_proprietario = Proprietario(nome, tipo_pessoa, doc_identificacao, data, endereco, telefone, email)
  proprietarios.append(novo_proprietario)
  print("DADOS CADASTRADOS")
  print()
  print(novo_proprietario)
  return novo_proprietario

def cadastroCorretor():  #Cadastrar Corretor
  print("Preencha os campos abaixo:")
  print("CAMPO CORRETOR")
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
  print("DADOS CADASTRADOS")
  print()
  print(novo_corretor)  


def busca_proprietario():
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
# def encerrarSistema(): #Sair
#   print("Encerrando....")

def busca_corretor():
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

def busca_cliente():  
  print("-- DADOS CLIENTE --") 
  doc_identificacao = str(input("CPF/CNPJ: "))
  if len(clientes) <= 0:
    novoCliente = cadastroCliente()
  else:   
    for cliente in clientes:
      if cliente.doc_identificacao == doc_identificacao:
        novoCliente = cliente
        break       
    if not novoCliente:        
      novoCliente = cadastroCliente()
      
  print("Cliente vinculado.")
  return novoCliente  

  
clientes = list()
proprietarios = list()
corretores = list()
