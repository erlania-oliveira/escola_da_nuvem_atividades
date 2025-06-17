'''4- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
'''
def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

temp = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C, F ou K): ").upper()
destino = input("Unidade de destino (C, F ou K): ").upper()

if origem == destino:
    resultado = temp
elif origem == 'C':
    if destino == 'F':
        resultado = celsius_to_fahrenheit(temp)
    elif destino == 'K':
        resultado = celsius_to_kelvin(temp)
    else:
        resultado = None
elif origem == 'F':
    if destino == 'C':
        resultado = fahrenheit_to_celsius(temp)
    elif destino == 'K':
        resultado = fahrenheit_to_kelvin(temp)
    else:
        resultado = None
elif origem == 'K':
    if destino == 'C':
        resultado = kelvin_to_celsius(temp)
    elif destino == 'F':
        resultado = kelvin_to_fahrenheit(temp)
    else:
        resultado = None
else:
    resultado = None

if resultado is not None:
    print(f"{temp}°{origem} equivalem a {resultado:.2f}°{destino}")
else:
    print("Unidade inválida! Use C, F ou K.")
