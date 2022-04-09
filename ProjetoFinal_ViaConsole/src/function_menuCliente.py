from pessoa import Cliente
from functions import menuAnterior

def cadastroCliente():  #Cadastrar CLIENTE/INQUILINO
  print("---------------------------")   
  print("---------NOVO CLIENTE-------")
  nome = str(input("Nome/Razão Social: ")).upper()
  tipo_pessoa = str(input("Pessoa Fisica ou Juridica: "))
  doc_identificacao = str(input("CPF/CNPJ: "))
  data = str(input("Data de Nascimento ou Fundação: "))
  endereco = str(input("Rua/Nº/Bairro/Cidade/UF: ")) 
  telefone = str(input("DDD+Telefone: "))
  email = str(input("Email: ")) 
  novo_cliente = Cliente(nome, tipo_pessoa, doc_identificacao, data, endereco, telefone, email)
  clientes.append(novo_cliente)
  print("***** DADOS CADASTRADOS *****")
  print()
  print(novo_cliente)
  return novo_cliente

def listaCliente(): #Verificar Lista de Clientes
  if len(clientes) <= 0:
    print("Nenhum cliente cadastrado")
  else:
    print("-------------------------------")
    print("       LISTA DE CLIENTES       ")
    print("-------------------------------")
    for cliente in clientes:
      print(cliente)
      print()

def busca_cliente():
  novoCliente = None  
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

def escolhaCliente(opcao1):    
  if opcao1 in [1,2,3,0]:    
    if opcao1 == 1: #Cadastro Cliente
      cadastroCliente()
      
    elif opcao1 == 2: #Lista de Cliente  
      listaCliente()
        
    elif opcao1 == 3: #Deletar Cliente
      deletarCliente()

    elif opcao1 == 0:#Retornar
      menuAnterior()
      return True
    
  else:
    print("Opção Inválida!")
    return False

def deletarCliente():
  clienteDel = False
  print("-- Para DELETAR CLIENTE, preencha os dados abaixo: --")  
  doc_identificacao = str(input("CPF/CNPJ: "))
  if len(clientes) <= 0:
    print("Corretor não localizado!")
  else:   
    for cliente in clientes:
      if cliente.doc_identificacao == doc_identificacao:
        clientes.remove(cliente)
        print("Cliente excluído!")
        clienteDel = True
        break
    if clienteDel == False:        
      print("Cliente não localizado!")

clientes = list()