'''Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'. O programa deve exibir o nome, email e país do usuário gerado.'''
import requests
import random
import string

try:
    # Faz requisição à API
    resposta = requests.get("https://randomuser.me/api/")
    resposta.raise_for_status()  # Gera erro se a resposta for ruim

    # Converte a resposta JSON
    dados = resposta.json()
    usuario = dados['results'][0]

    # Extrai nome, email e país
    nome = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario['email']
    pais = usuario['location']['country']

    # Exibe os dados
    print("Perfil de Usuário Gerado:")
    print(f"Nome: {nome}")
    print(f"Email: {email}")
    print(f"País: {pais}")

except requests.exceptions.RequestException as erro:
    print("Erro ao acessar a API:", erro)
except KeyError:
    print("Erro ao interpretar a resposta da API.")
