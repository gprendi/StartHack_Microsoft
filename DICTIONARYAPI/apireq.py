#from config import Config
import requests
import json

def request_definition(word):
        #config = Config()
        response = requests.get('https://www.dictionaryapi.com/api/v3/references/medical/json/%s?key=%s'%
            (word,API_KEY))
        text= response.json()
        #loaded = text[-1]['shortdef']
        #result =(word.title() + ': ')
        #for i in loaded:
        #    result += i + '\n'
        #return result
        loaded= text[0]['def'][0]['sseq'][0][0][1]['dt'][0][1]
        return loaded




        



