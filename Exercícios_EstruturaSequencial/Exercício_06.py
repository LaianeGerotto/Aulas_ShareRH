#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área
from cmath import pi


raio = float(input("Digite o raio de um círculo: "))
area = pi * (raio*raio)
print(f"A área do círculo será de {area:,.2f}.")