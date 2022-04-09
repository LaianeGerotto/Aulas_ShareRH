
from functions import menuAnterior
from function_menuCliente import escolhaCliente
from function_menuCorretor import escolhaCorretor
from function_menuProprietario import escolhaProprietario


def menuPessoas():
  while True:
    print("Escolha uma das opções abaixo:")
    print("1 - CLIENTE/INQUILINO")
    print("2 - PROPRIETÁRIO")
    print("3 - CORRETOR")
    print("0 - Retornar ao Menu anterior/Encerrar")
    opcao = int(input("Opção: "))
    if escolhaMenuPessoas(opcao):
        break

def escolhaMenuPessoas(opcao):    
  if opcao in [1,2,3,0]:    
    if opcao == 1: #CLIENTE/INQUILINO
      while True:
        print("Escolha uma das opções abaixo:")
        print("1 - Cadastro Cliente")
        print("2 - Lista de Clientes")
        print("3 - Deletar Cliente")
        print("0 - Retornar ao Menu anterior/Encerrar")
        opcaoCliente = int(input("Opção: "))
        if escolhaCliente(opcaoCliente):
          break
       
    elif opcao == 2: #PROPRIETÁRIO    
      while True:
        print("Escolha uma das opções abaixo:")
        print("1 - Cadastro Proprietário")
        print("2 - Lista de Proprietários")
        print("3 - Deletar Proprietário")
        print("0 - Retornar ao Menu anterior/Encerrar")
        opcaoProprietario = int(input("Opção: "))
        if escolhaProprietario(opcaoProprietario):
          break    

    elif opcao == 3: #Cadastrar CORRETOR  
      while True:
        print("Escolha uma das opções abaixo:")
        print("1 - Cadastro Corretor")
        print("2 - Lista de Corretores")
        print("3 - Deletar Corretor")
        print("0 - Retornar ao Menu anterior/Encerrar")
        opcaoCorretor = int(input("Opção: "))
        if escolhaCorretor(opcaoCorretor):
          break                  
      
    elif opcao == 0:# Retornar
      menuAnterior()
      return True    
  
  else:
    print("Opção Inválida!")
    return False




  



  



