'''Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.'''

print('-'*35)
print(" Converter Celsius para Fahrenheit ")
print('-'*35)

celsius = float(input("Digite a temperatura em °C: "))
fahrenheit = (celsius * 9/5) + 32
print(f"A temperatura {celsius:.1f}°C corresponde a {fahrenheit:.1f}°F.")