from pessoa import Pessoa,Cliente, Proprietario, Corretor

print("PAINEL DE CADASTRO")

def cadastro():
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
      opcao1()
      
    elif opcao == 2: #Cadastrar PROPRIETÁRIO    
      opcao2()      

    elif opcao == 3: #Cadastrar CORRETOR  
      opcao3()                   
        
    elif opcao == 0:#Sair
      opcao0()
      return True    
  else:
    print("Opção Inválida!")
    return False


def opcao1():  #Cadastrar CLIENTE/INQUILINO
  print("Preencha os campos abaixo:")
  print("CAMPO CLIENTE")
  nome = str(input("Nome/Razão Social: ")).upper()
  tipo_pessoa = str(input("Pessoa Fisica ou Juridica: "))
  doc_identificacao = str(input("CPF/CNPJ: "))
  data = str(input("Data de Nascimento ou Fundação: "))
  endereco = str(input("Rua/Nº/Bairro/Cidade/UF: ")) 
  telefone = str(input("DDD+Telefone: "))
  email = str(input("Email: ")) 
  novo_cliente = Cliente(nome, tipo_pessoa, doc_identificacao, data, endereco, telefone, email) #nome_fiador, doc_identificacao_fiador, data_fiador, endereco_fiador, telefone_fiador,email_fiador)
  cliente.append(novo_cliente)
  print("DADOS CADASTRADOS")
  print()
  print(novo_cliente)


def opcao2():  #Cadastrar PROPRIETÁRIO
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

def opcao3():  #Cadastrar Corretor
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
  proprietarios.append(novo_corretor)
  print("DADOS CADASTRADOS")
  print()
  print(novo_corretor)  

def opcao0(): #Sair
  print("Encerrando....")


 
cliente = list()
proprietarios = list()
corretor = list()
#cadastro()