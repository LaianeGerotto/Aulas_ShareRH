'''Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.'''
print('-'*35)
print(" Converter Fahrenheit para Celsius ")
print('-'*35)

fahrenheit = float(input("Digite a temperatura em °F : "))
celsius = 5 *((fahrenheit - 32)/9)
print(f"A temperatura {fahrenheit:.1f}°F corresponde a {celsius:.1f}°C")


