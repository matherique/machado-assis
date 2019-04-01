#!/usr/bin/env python3
from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
import json 
from unidecode import unidecode
import requests

# baixando o arquivo em formato pdf e salvando na pasta
def downloadfile(link, name, folder):
    r = requests.get(link, allow_redirects=True)
    open('../download/{}/{}.pdf'.format(folder, name), 'wb').write(r.content)
    print("download finished - ../download/{}/{}.pdf".format(folder, name))

# pegando dados do json com os links 
def getdados():
    machado = open('machado.json', 'r')
    dados = json.load(machado)
    machado.close()
    return dados

# formata nome da obra
def formatname(name):
    semacentos = ' '.join(list(map(unidecode, name.split(' '))))
    return semacentos.replace('-', '').replace(',','').replace(' – ', ' ').replace('.', '').replace(' ', '-').replace('/', '').lower()

# scrappping todas as obras com base nos links
def getallworks():        
    dados = getdados()
    
    for categoria in dados.keys():
        url = dados[categoria]['link']
       
        html = urlopen(url)
        res = BeautifulSoup(html.read(), "html5lib")
        # pegando nome das obras
        nomes = res.findAll("div", { "class" : "detalhes" })
        
        # pegando todos os links das obras 
        for i, div in enumerate(res.findAll("div", {"class" : "download"})):
            link = div.find('a').get('href')
            nome = nomes[i].findAll('div', { 'class' : 'titulo' })[0].text
            info = { 'link' : link, 'nome': nome.strip() }
            # salvando no dict dados o link de download e nome 
            dados[categoria]['obras'].append(info)

    # formatando link e baixando todos os pdf
    for cat in dados.keys():
        obras = dados[cat]['obras']
        for obra in obras:
            link = "http://machado.mec.gov.br{}".format(obra['link'])
            nome = formatname(obra['nome'])
            downloadfile(link, nome, cat)

if __name__ == '__main__':
    getallworks()

