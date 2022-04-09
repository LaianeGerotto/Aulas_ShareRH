import getpass

from usuario import Usuario
# from function_cadastroPessoa import menuPessoas
# from function_cadastroImoveis import menuImoveis
# from function_contratos import menuContratos

def menuPrincipal():
  while True:
    print("1 - Novo usuário")
    print("2 - Já sou cadastrado")
    print("0 - Encerrar")
    opcao01 = int(input("Opção: "))
    if opcoesMenuPrincial(opcao01):
      break

def opcoesMenuPrincial(opcao01):    
  if opcao01 in [1,2,0]:    
    if opcao01 == 1: #Novo usuário
      novoUsuario()
      
    elif opcao01 == 2: #Já sou cadastrado     
      if usuarioJaCadastrado():
        menuNavegacao()
        
    elif opcao01 == 0:#Sair
      encerrarSistema()
      return True
    
  else:
    print("Opção Inválida!")
    return False

def novoUsuario():  #Novo usuário
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
    
def usuarioJaCadastrado(): #Já possui cadastro
  verificacao2 = False
  while not verificacao2:
    print("Para acessar o sistema, insira as informações abaixo: ")    
    email = input("Email: ")    
    senha = getpass.getpass("Senha: ")
    for usuario in usuarios:
      if usuario.email == email and usuario.senha == senha:
          print("Acesso liberado!")
          verificacao2 = True          
          return usuario
    if not verificacao2:
      print("Email e/ou senha inválida!")
      return None     

def encerrarSistema(): #Sair
  print("Até breve!")
  
def menuNavegacao():
  while True:
    print("--  PAINEL DE GERENCIAMENTO  --")
    print("Para iniciar, informe a opção desejada: ")
    print("1 - Cadastro de Corretor/Cliente/Proprietário")
    print("2 - Cadastro de Imóveis")
    print("3 - Cadastro de Contratos")
    print("0 - Encerrar")
    opcao02 = int(input("Opção: "))
    if opcoesMenuNavegacao(opcao02):
      break


def opcoesMenuNavegacao(opcao02):    
  if opcao02 in [1,2,3,0]:    
    if opcao02 == 1: #Cadastro de Corretor/Cliente/Proprietário
      menuPessoas()
      
    elif opcao02 == 2: #Cadastro de Imóveis     
      menuImoveis()
        #menuNavegacao()

    elif opcao02 == 3: #Cadastro de Contratos
      menuContratos()
    
        
    elif opcao02 == 0:#Sair
      encerrarSistema()
      return True
    
  else:
    print("Opção Inválida!")
    return False


usuarios = list()

