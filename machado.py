#!/usr/bin/env python3
import glob
obras = glob.glob('obras/*.txt')


def filterlist(func, l):
    return list(filter(func, l))

ARQUIVO = 'dados.csv'
DADOS = []
TOTAL = 0

for obra in obras:
    with open(obra, 'r') as fp:
        lines = fp.readlines()
        nonewline = list(map(lambda x : x.replace("\n", ""), lines))
        
        toremove = ['.','','-','(',')',',',';',':','|','!','"','#','$','%','&','/','=','?','~','^','>','<','ª','º','Š','\x0c','—']
        
        for r in toremove:
             nonewline = list(map(lambda x: x.replace(r, '').strip() , nonewline))
        
        nocap = filterlist(lambda x: x.find('CAPÍTULO') < 0, nonewline)
        nowhitespace = filterlist(lambda x: x != '', nocap)
        noend = filterlist(lambda x: x != 'FIM', nowhitespace)
        words = [word for line in noend for word in line.split(' ')]
        TOTAL += len(words)

        name = obra.split('/')[1:][0][:-4].replace('-', ' ').upper()
        print("{} - {} palavras".format(name, len(words)))

        DADOS += words

print("="*50)
print("Total de palavras: {}".format(TOTAL))


with open(ARQUIVO, 'w') as fp:
    fp.write(';'.join(DADOS))
