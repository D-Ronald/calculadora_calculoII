import requests
import plotly.graph_objects as go
from plotly.offline import plot
import json

f = 'x+y'
x = 1
y = 2

def get_plano_tangente():
    URL = "https://3d7d8b0c-4e24-47a6-8778-aa1b83fd2932-00-3mctl2qlxcx1v.picard.replit.dev/plano_tangente"
    parametros = {'function' : f, 'x': x, 'y': y}
    response = requests.get(URL, params= parametros)
    return response

def get_reta_normal():
    URL = "https://3d7d8b0c-4e24-47a6-8778-aa1b83fd2932-00-3mctl2qlxcx1v.picard.replit.dev/reta_normal"
    parametros = {'function' : f, 'x': x, 'y': y}
    response = requests.get(URL, params= parametros)
    return response

def get_derivada_em_x():
    URL = "https://3d7d8b0c-4e24-47a6-8778-aa1b83fd2932-00-3mctl2qlxcx1v.picard.replit.dev/derivada_em_x"
    parametros = {'function' : f, 'x': x, 'y': y}
    response = requests.get(URL, params= parametros)
    return response

def get_grafico():
    URL = "https://3d7d8b0c-4e24-47a6-8778-aa1b83fd2932-00-3mctl2qlxcx1v.picard.replit.dev/maximos_minimos"
    parametros = {'function' : f}
    response = requests.get(URL, params= parametros)
    return response

def get_derivadas_implicitas():
    URL = "https://calculo-918390110613.us-central1.run.app/plano_tangente"
    parametros = {'function' : f, 'x': x, 'y': y}
    response = requests.get(URL, params= parametros)
    return response

response = get_grafico()
# Imprimir o conteúdo da resposta


if response.status_code == 200:
    print(response.text)
    with open('src/index.html', 'w') as file:
        file.write(response.text)
else:
    print(f"Erro ao fazer a requisição: {response.status_code}")