#!/usr/bin/env python3
import glob
from nltk.tokenize import TweetTokenizer
import json
import re
import numpy as np 

token = TweetTokenizer(strip_handles=True, reduce_len=True)

# todos os arquivos .txt
obras = glob.glob('obras/*.txt')
palavras = []

def addtokenpontuacao(text):
    lp = token.tokenize(text)
    pontuacoes = json.loads(open('tokens.json','r').read())
    
    # percorrendo todas as palavras e trocando por token de pontuacao
    for i, p in enumerate(lp):
        lp[i] = pontuacoes[p] if p in pontuacoes.keys() else p

    return lp

# tokeninzando palavras
for obra in obras:
    texto = open(obra, 'r').read().lower().replace("\n", " ")
    palavras += addtokenpontuacao(texto)



print(palavras)
