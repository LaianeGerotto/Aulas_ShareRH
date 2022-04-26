def inicia_tabuada():
  for i in range(11):
    imprime_linha_tabuada(i)
  print("Sucesso!")


def imprime_linha_tabuada(i):
  for j in range(11):
      print(f"{i} x {j} = {i*j}")
  print("\n")


def tabuada():
  while True:
    print("Selecione uma opção:")
    print("1 - Multiplicar")
    print("2 - Sair")
    opcao = int(input(""))
    if opcao in [1,2]:
          if opcao == 1: 
              print("Iniciando a multiplicação")
              # 4 x 4 = 16
              inicia_tabuada()
          elif opcao == 2:
            print("Saindo do sistema...")
            break          
    else:
      print("Opção Inválida!")
 

usuario = input("Entre com o seu nome: ")
print(f"Seja Bem-vindo {usuario}!\n")
tabuada()
