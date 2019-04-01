#!/usr/bin/env python3
import glob
from nltk.tokenize import TweetTokenizer
token = TweetTokenizer(strip_handles=True, reduce_len=True)

# todos os arquivos .txt
obras = glob.glob('obras/*.txt')

# utils para facilitar a filtragem
def filterlist(func, l):
    return list(filter(func, l))

ARQUIVO = 'dados.csv'
DADOS = []
TOTAL = 0

for obra in obras:
    with open(obra, 'r') as fp:
        lines = fp.readlines()
        # removendo todos os \n
        nonewline = list(map(lambda x : x.replace("\n", ""), lines))
                   
        # removendo linha do capitulo
        nocap = filterlist(lambda x: x.find('CAPÍTULO') < 0, nonewline)
        
        # removendo espaco em branco
        nowhitespace = filterlist(lambda x: x != '', nocap)
        
        # removendo linha do FIM
        noend = filterlist(lambda x: x != 'FIM', nowhitespace)

        tokenized = token.tokenize('\n'.join(noend))
        TOTAL += len(tokenized)
        print(len(tokenized))   




print("Total de palavras: {}".format(TOTAL))
