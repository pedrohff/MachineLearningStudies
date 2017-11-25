# Conjunto de importações
# Caminho base para requisitar a Graph API
# Autor: Ricardo Roberto de Lima. - Data: 01/08/2017
# Programa: Responsável por coletar dados via pesquisa genérica do face..

#Conjunto de importações
import requests
import json

base_url = "https://graph.facebook.com/search"

q = "python"
#tipo = "page"
#tipo = "event"
tipo = "group"

#O objeto receberá o ID da página 
access_token = 'EAAPdr20B97oBAMFJImhCveUIuyUcFGTkwrbmsALvdEuWFZAWDZAdc2L0ueLNSXPcGIKaFUuzSYozCBZCXx6qyr5FAMk2M3Wb9Naorjx7dzhhXOBs4rLHZBCNOGoXUcRrspWznZBhlkEUQQr3kweO72RIzXtU8Paoqn19vvZBB4K0Vw0ptO0O8ZCBuifqnd7dYShNXlG6Of67x7c9jGnZBZBhOiL8zZBjWNnFr6HQwsh1AXMgZDZD'

url = "%s?q=%s&type=%s&access_token=%s" % (base_url, q, tipo, access_token) 
print(url)
#Envia a requisição

#Armazena a resposta na variável dados
dados = requests.get(url).json()

#Apresenta a resposta no formato JSON identadamente
print (json.dumps(dados, indent=4))

