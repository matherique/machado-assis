#!/usr/bin/env python3
from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
import json 
from unidecode import unidecode
import requests

def downloadfile(link, name, folder):
    r = requests.get(link, allow_redirects=True)
    open('download/{}/{}.pdf'.format(folder, name), 'wb').write(r.content)
    print("download finished - download/{}/{}.pdf".format(folder, name))

def getdados():
    machado = open('machado.json', 'r')
    dados = json.load(machado)
    machado.close()
    return dados

def formatname(name):
    semacentos = ' '.join(list(map(unidecode, name.split(' '))))
    return semacentos.replace('-', '').replace(',','').replace(' – ', ' ').replace('.', '').replace(' ', '-').replace('/', '').lower()

def getallworks():        
    dados = getdados()

    for categoria in dados.keys():
        url = dados[categoria]['link']
       
        html = urlopen(url)
        res = BeautifulSoup(html.read(), "html5lib")
        nomes = res.findAll("div", { "class" : "detalhes" })
        
        for i, div in enumerate(res.findAll("div", {"class" : "download"})):
            link = div.find('a').get('href')
            nome = nomes[i].findAll('div', { 'class' : 'titulo' })[0].text
            info = { 'link' : link, 'nome': nome.strip() }
            dados[categoria]['obras'].append(info)


    for cat in dados.keys():
        obras = dados[cat]['obras']
        for obra in obras:
            link = "http://machado.mec.gov.br{}".format(obra['link'])
            nome = formatname(obra['nome'])
            downloadfile(link, nome, cat)


getallworks()

