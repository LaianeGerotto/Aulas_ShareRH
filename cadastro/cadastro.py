def cadastro():
  while True:
      print("Selecione uma opção:")
      print("1 - Cadastrar")
      print("2 - Listar")
      print("3 - Sair")
      opcao = int(input(""))
      if escolha(opcao):
        break
     

def escolha(opcao):  
  if opcao in [1,2,3]:
    if opcao == 1: #Cadastrar
        nome = ""
        data_nasc = ""
        endereco = ""
        while nome == "":
            nome = input("Coloque o nome: ")
        while data_nasc == "":
            data_nasc = input("Coloque a data de nascimento: ")
        while endereco == "":
            endereco = input("Coloque o endereço: ")

        registro = {"Nome":nome, "Data_Nascimento":data_nasc, "Endereco": endereco}
        lista.append(registro)
        print("Sucesso! Cadastrado!")
        return False
    elif opcao == 2: #Listar
        for item in lista:
            print(item)
        return False
        
    elif opcao == 3:#Sair
        print("Saindo do sistema...")
        return True
  else:
      print("Opção Inválida!")
      return False

lista = []
usuario = input("Entre com o seu nome: ")
print(f"Seja Bem-vindo {usuario} !\n")
cadastro()