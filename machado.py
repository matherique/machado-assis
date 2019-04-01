#/usr/bin/env python3
import glob

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
        
        toremove = ['.','','-','(',')',',',';',':','|','!','"','#','$','%','&','/','=','?','~','^','>','<','ª','º','Š','\x0c','—']
        
        # removendo todos os caracteres especiais
        for r in toremove:
             nonewline = list(map(lambda x: x.replace(r, '').strip() , nonewline))
        
        # removendo linha do capitulo
        nocap = filterlist(lambda x: x.find('CAPÍTULO') < 0, nonewline)
        
        # removendo espaco em branco
        nowhitespace = filterlist(lambda x: x != '', nocap)
        
        # removendo linha do FIM
        noend = filterlist(lambda x: x != 'FIM', nowhitespace)
 
        # criando lista com todas as palavras das linhas
        words = [word for line in noend for word in line.split(' ')]

        # contando total de palavras
        TOTAL += len(words)
        
        # formatando o nome e mostrando a quantidade de palavra
        name = obra.split('/')[1:][0][:-4].replace('-', ' ').upper()
        print("{} - {} palavras".format(name, len(words)))
        # salvando todas as palavras de uma obra 
        DADOS += words

print("="*50)
print("Total de palavras: {}".format(TOTAL))

# salvando as palavras em um csv
with open(ARQUIVO, 'w') as fp:
    fp.write(';'.join(DADOS))
