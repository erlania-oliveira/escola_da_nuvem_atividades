'''4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

Distância percorrida: 300 km

Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
'''

distancia = 300.0         # em km
combustivel_gasto = 25.0  # em litros

consumo_medio = distancia / combustivel_gasto

print("Dados da viagem:")
print(f"Distância percorrida: {distancia:.2f} km")
print(f"Combustível gasto: {combustivel_gasto:.2f} litros")
print(f"Consumo médio: {consumo_medio:.2f} km/l")
