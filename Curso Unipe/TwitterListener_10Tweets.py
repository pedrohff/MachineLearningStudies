# Conjunto de importações da biblioteca Tweepy
# Coletando os dados com os campos específicos do Twiiter.
# Autor: Ricardo Roberto de Lima. - Data: 01/08/2017
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

class TwitterListener_10Tweets(StreamListener):  
    #método de inicialização   
    def __init__(self):
        #contador de tweets
        self.cont_tweet = 0
        #valor máximo de tweets a serem coletados
        self.max_tweets = 100 
        
    def on_data(self, data):
        #incrementa o contador de tweets
        self.cont_tweet = self.cont_tweet + 1
        try:
            #carrega e codifica os dados para o formato JSON
            tweet = json.loads(data)
            #Escreve o campo de data de publicação do tweet
            print("Data da publicacao do tweet")            
            print(tweet.get('created_at'))
            #Escreve o campo referente ao conteúdo do tweet
            print("Conteudo do tweet")
            print(tweet.get('text'))
            #Escreve o campo referente ao idioma do tweet
            print("Idioma do tweet")
            print(tweet.get('lang'))
            #Escreve o campo referente ao total de likes que o tweet recebeu
            print("Total de likes do tweet")
            print(tweet.get('favorite_count'))
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

    tl = TwitterListener_10Tweets()
    oauth = OAuthHandler(consumer_key, consumer_secret)
    oauth.set_access_token(access_token, access_token_secret)

    stream = Stream(oauth, tl)
    stream.filter(track=['enem'])

#chamada da função coletar_tweets()
coletar_tweets()
