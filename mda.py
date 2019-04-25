#!/usr/bin/env python3
import glob
from nltk.tokenize import TweetTokenizer
import json
import re
import numpy as np 

token = TweetTokenizer(strip_handles=True, reduce_len=True)

# pega lista de todos os arquivos .txt
obras = glob.glob('obras/*.txt')
palavras = []

def addtoken(text):
    lp = token.tokenize(text)
    pontuacoes = json.loads(open('tokens.json','r').read())
    
    # troca a pontuacao por tokens 
    for i, p in enumerate(lp):
        lp[i] = pontuacoes[p] if p in pontuacoes.keys() else p

    return lp

# pega conteudo dos textos e tokeniza o conteudo
for obra in obras:
    texto = open(obra, 'r').read().lower().replace("\n", " ")
    palavras += addtoken(texto)

print(palavras)
print("="*50)
print("Quantidade de palavras: {}".format(len(palavras)))
