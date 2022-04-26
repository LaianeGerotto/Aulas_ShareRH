'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
   Calcule e mostre o total do seu salário no referido mês.'''
print("-"*25)
print(" Calculadora de Salário ")
print("-"*25)
valor = float(input("- Quanto você ganha por hora? R$ "))
hora = float(input("- Quantas horas você trabalha no mês? "))
salario = valor * hora
print(f"Seu salário é de R$ {salario:,.2f}")
