#Conjunto de importação
# Implementação do Código para Captura dos Dados no Twitter e gravação em arquivo do tipo CSV..
import csv
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

class TwitterListener(StreamListener):  
    #método de inicialização   
    def __init__(self):
        self.cont_tweet = 0
        self.max_tweets = 10000 
        
    def on_data(self, data):
        #incrementa o contador de tweets
        self.cont_tweet = self.cont_tweet + 1
        try:
            print(data)
            #converte o tweet para o formato json
            tweet = json.loads(data) 

            #cria e carrega o arquivo 'twitter_data_csv.csv'
            meu_arquivo = open('twitter_data_sabado.csv', mode='a', encoding='utf-8')
            #cria o objeto writer para escrever no arquivo
            writer = csv.writer(meu_arquivo) 
            #escreve os dados dos campos 'created_at' e 'text' no arquivo csv
            writer.writerow([tweet.get('created_at'), tweet.get('text')])
 
            #fecha a referência para o arquivo
            meu_arquivo.close()
        except BaseException as erro:
            print('Erro: ' + erro)
        #condição de parada
        if self.cont_tweet >= self.max_tweets:
            #retorne false
            return False

def coletar_tweets():
    #Complete aqui com o valor da "access_token" gerada para você
    access_token = "77266017-BoJAB4fwsaKtEHJT2OQUsGpMfZwP8ebt7LQUdgxHP"
    #Complete aqui com o valor da "access_token_secret" gerada para você
    access_token_secret = "alR6yKuCW9yU3bfoDNs8YRGRzPhgfvECiDweN84ikkLaz"
    #Complete aqui com o valor da "consumer_key" gerada para você
    consumer_key = "7M4rxjVVGTcMt5b5q2zzx4H8P"
    #Complete aqui com o valor da "consumer_secret" gerada para você
    consumer_secret = "dzZ5l5aRYkrimPkPTUqERl1IQe7hcMYzolQ3kg1g2MDU0BKeOT"

    tl = TwitterListener()
    oauth = OAuthHandler(consumer_key, consumer_secret)
    oauth.set_access_token(access_token, access_token_secret)

    stream = Stream(oauth, tl)
    stream.filter(track=['enem'])

#chamada da função coletar_tweets()
coletar_tweets()
