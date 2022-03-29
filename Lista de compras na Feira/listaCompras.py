'''
Faça um programa que monte uma lista de compras na feira. Nesse programa deverá conter:
-Uma tela para mostrar a lista de compras
-Outra tela para cadastrar um item dessa lista
-Outra tela para excluir um item (Deverá primeiro mostrar a lista e depois excluir o item conforme posição)
-Login ao começar
-Opção Sair do programa
Dicas:
Use Lista
Não necessita de usar funções, mas pode usar se achar necessário
Não necessita criar classes, mas pode usar se achar necessário
Use como base, os exercicios anteriores para montar o programa (Tabuada e o do Troubleshooting feito em sala de aula)
Use funções de listas'''

def cadastro():
  while True:
    print("Selecione uma opção:")
    print("1 - Verificar Lista")
    print("2 - Cadastrar item")
    print("3 - Excluir item")
    print("4 - Sair")
    opcao = int(input("Opção: "))
    print("-"*50)
    if escolha(opcao):
      break


def escolha(opcao):
  if opcao in [1,2,3,4]:    
      if opcao == 1: #Verificar Lista
        opcao1()
        
      elif opcao == 2: #Cadastrar Item      
        opcao2()
            
      elif opcao == 3: #Deletar item
        opcao3()        
          
      elif opcao == 4:#Sair
        opcao4()
        return True
  else:
    print("Opção Inválida!")
    return False


def opcao1():#Verificar Lista
  if len(lista) == 0:
    print("   Sua lista está vazia!")
    print("-"*50)
  else:
    contador = 1
    for item in lista:
      print(f"{contador} - {item}")
      contador += 1
      print("-"*50)


def opcao2(): #Cadastrar Item 
  produto = ""
  qtde = ""
  while produto == "":
    produto = input("Insira o item: ")
  while qtde == "":
    qtde = input(f"Qual a quantidade do item {produto}: ")
  registro = {"Item":produto, "Quantidade":qtde}
  lista.append(registro)
  print("Item Cadastrado!")
  print("-"*50)


def opcao3(): #Deletar item
  posicao = int(input("Qual item da lista deseja excluir? "))
  if posicao > len(lista):
    print(f"Sua lista não contém o item {posicao}!")
    print("")
    for item in lista:
        print(item)
        print("-"*50)       
  elif posicao > 0:
    del lista[posicao-1]
    print("Item excluido com sucesso!")
    print("-"*50)


def opcao4(): #Sair
  print("Encerrando a lista...")

lista = []
login = input("Informe seu nome: ")
print("-"*50)
print(f" {login}, Seja bem vindo(a) a sua Lista de Compras!")
print("-"*50)
cadastro()