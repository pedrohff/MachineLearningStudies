# Conjunto de importações
# Implementação do Código para Captura dos Dados no Twitter e gravação em arquivo do tipo Json..
# Autor: Ricardo Roberto de Lima. - Data: 01/08/2017
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from collections import namedtuple

class TwitterListener(StreamListener):
    #método de inicialização   
    def __init__(self):
        #contador de tweets
        self.cont_tweet = 0
        #valor máximo de tweets a ser coletado
        self.max_tweets = 10000
        
    def on_data(self, data):
        tweet = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        
        try:
            if ('RT @' not in tweet.text) and (tweet.retweeted==False):
                self.cont_tweet = self.cont_tweet + 1
                print(str(self.cont_tweet) + "\n" + tweet.text)
                #converte o tweet para o formato json
                #cria e carrega o arquivo 'twitter_data.json'
                #o argumento mode='a' indica que será realizada a operação append
                with open('twitter_enem2.json', mode='a') as meu_arquivo:
                    #salva o tweet no arquivo com identação
                    json.dump(tweet, meu_arquivo, indent=4) 
        except BaseException as erro:
            print(erro)
        except AttributeError as e:
            print('Tweet mal formatado')
        except TypeError as erro:
            print(erro)
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
    stream.filter(track=['#tamojuntoenem'])

#chamada da função coletar_tweets()
coletar_tweets()
