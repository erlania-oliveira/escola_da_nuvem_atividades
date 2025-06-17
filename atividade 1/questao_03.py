'''3- Calculadora de Volume

Crie um programa que calcula o volume de uma caixa retangular. Use as seguintes dimensões:
Comprimento: 12 cm
Largura: 14 cm
Altura: 20 cm O programa deve calcular o volume e exibir o resultado em cm³.
'''
def calcular_volume(comprimento, largura, altura):
    volume = comprimento * largura * altura
    return volume
resultado = calcular_volume(12, 14, 20)
print("O volume da caixa é:", resultado, "cm³")