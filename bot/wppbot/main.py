from wppbot import facebook_bot #importa as funções
import json #importa a livraria pra ler aquivos em json
import time

if __name__ == "__main__": #comportamento principal
    with open('config.json') as file: #abrir o json como arquivo
    		config = json.load(file) #variavel config recebe dados do arquivo json carregado
    
    driver = config['driver'] #set variavel driver com os dados de 'driver' dentro do arquivo json
    url =  config['url'] #set variavel url com os dados de 'ur' dentro do arquivo jsone
    username = config['username'] #set variavel username com os dados de 'username' dentro do arquivo json
    password = config['password'] #set variavel password com os dados de 'password' dentro do arquivo json
    texto = input('qual texto quer enviar?: ')
    facebook_bot(driver,url,username,password).spam(texto) # executa a função facebook_bot com os dados recebidos do arquivo json
