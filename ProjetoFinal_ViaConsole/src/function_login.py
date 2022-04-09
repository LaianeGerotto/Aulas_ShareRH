import getpass
from src.usuario import Usuario

def escolha():
  while True:
    print("1 - Novo usuário")
    print("2 - Já sou cadastrado")
    print("0 - Encerrar")
    opcao = int(input("Opção: "))
    if opcoes(opcao):
      break

def opcoes(opcao):    
  if opcao in [1,2,0]:    
    if opcao == 1: #Novo usuário
      opcao1()
      
    elif opcao == 2: #Já sou cadastrado     
      opcao2()      
        
    elif opcao == 0:#Sair
      opcao0()
      return True
    
  else:
    print("Opção Inválida!")
    return False

def opcao1():  #Novo usuário
  print("Preencha os campos abaixo:")
  nome = str(input("Usuário: "))
  email_ok = False      
  while not email_ok:
    email = str(input("Email: "))
    email_ok = True 
    for usuario in usuarios:       
      if usuario.email == email:          
        print("Email já cadastrado!")
        email_ok = False
        break               

  while True:
    senha = getpass.getpass("Senha: ")
    confirmacao_senha = getpass.getpass("Confirme sua senha: ")
    if senha != confirmacao_senha:
      print("Senha divergente!")
    else:
      print("Cadastro realizado!")
      break
  novo_usuario = Usuario(nome, email, senha)
  usuarios.append(novo_usuario)    
    
def opcao2(): #Já possui cadastro
  verificacao2 = False
  while not verificacao2:
    print("Para acessar o sistema, insira as informações abaixo: ")    
    email = input("Email: ")    
    senha = getpass.getpass("Senha: ")
    for usuario in usuarios:
      if usuario.email == email and usuario.senha == senha:
          print("Acesso liberado!")
          verificacao2 = True
          break
    if not verificacao2:
      print("Email e/ou senha inválida!")
      #Habilitar de menu de cadastro de Pessoas e Imóveis    

def opcao0(): #Sair
  print("Até breve!")
  

usuarios = list()

