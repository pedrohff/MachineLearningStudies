# Conjunto de importações
# Caminho base para requisitar a Graph API
# Autor: Ricardo Roberto de Lima. - Data: 01/08/2017
# Programa: Responsável por coletar dados da pessoa como: curtidas (likes), reações (reactions), comentários (comments), publicações (posts) e (shares).
import requests
import json        

base_url = "https://graph.facebook.com/"
#Variável para definir a versão que queremos requisitar
versao = "v2.11/"
objeto = "193810163083"
#access_token = "329484294160599|RICnpAHDI6MEYxmx19Vb9aqKSDg"
access_token = "1088170447992762|685e2083a563e2e7316bd99459776a4f"
#Definição dos campos que iremos coletar
campos = "id,name,likes,posts"
#campos = "id,name,posts"
#campos = "likes"
#campos = "reactions"
#campos = "commets"
#campos = "sharedposts"

#A URL agora terá a variável campos
url = "%s%s?access_token=%s" % (base_url, objeto, access_token)

print(url)

#Envia a requisição
#Armazena a resposta na variável dados
dados = requests.get(url).json()
#Apresenta a resposta no formato JSON identadamente
print (json.dumps(dados, indent=4))


