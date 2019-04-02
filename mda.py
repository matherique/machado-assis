#!/usr/bin/env python3
import glob
from nltk.tokenize import TweetTokenizer
import json

token = TweetTokenizer(strip_handles=True, reduce_len=True)

# todos os arquivos .txt
obras = glob.glob('obras/*.txt')

# utils para facilitar a filtragem
def filterlist(func, l):
    return list(filter(func, l))

def filtrarlista(lista):
    # remover '' da lista
    filtro1 = list(filter(lambda p: p != '', lista))

    lista = filtro1

    return lista

ARQUIVO = 'dados.csv'
listapalavras = []
TOTAL = 0

for obra in obras:
    with open(obra, 'r') as fp:
        conteudo = fp.read()
        palavras = conteudo.replace('\n', ' ').split(' ')
        listapalavras += palavras

filtradas = filtrarlista(listapalavras[:1000])
print(filtradas)  


"""
    with open(obra, 'r') as fp:
        lines = fp.readlines()[:100]
        # removendo todos os \n
        nonewline = list(map(lambda x : x.replace("\n", ""), lines))
             
        #TODO: criar "token" dos <nome-do-simbolo-en>
        toremove = json.loads(open('tokens.json', 'r').read());
        # removendo todos os caracteres especiais


        for k, v in toremove.items():
             nonewline = list(map(lambda x: x.replace(k, v).strip() , nonewline))

        # removendo linha do capitulo
        nocap = filterlist(lambda x: x.find('CAPÍTULO') < 0, nonewline)
        
        # removendo espaco em branco
        nowhitespace = filterlist(lambda x: x != '', nocap)
        
        # removendo linha do FIM
        noend = filterlist(lambda x: x != 'FIM', nowhitespace)

        tokenized = token.tokenize('\n'.join(noend))
        TOTAL += len(tokenized)
        DADOS += tokenized
        print(tokenized)

print("Total de palavras: {}".format(TOTAL))


"""
