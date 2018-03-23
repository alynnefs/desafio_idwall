# -*- coding: utf-8 -*-
from lxml import html as _parse
import requests
import os
import sys

def listar(pesquisa):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'}
    _site = requests.get("https://www.reddit.com/r/%s" % pesquisa, headers=headers)
    _page = _site.text
    rr = _parse.fromstring(_page)
    a=rr.xpath('//*[@id="siteTable"]')

    texto = ""
    for b in a[0].xpath('div[*]'):
        try:
            try:
                upvotes = int(b.xpath('div[1]/div[3]')[0].text_content())
            except:
                if 'k' in b.xpath('div[1]/div[3]')[0].text_content():
                    upvotes = int(float(b.xpath('div[1]/div[3]')[0].text_content().replace('k',''))*1000)
                else:
                    upvotes = 0
            if upvotes >= 5000:
                try:
                    titulo = b.xpath('div[2]/div[1]/p[1]/a')[0].text_content()
                    subreddits = pesquisa
                    comentarios = b.xpath('div[2]/div/ul/li[1]/a')[0].items()[0][1]
                    linkThread = b.xpath('div[2]/div/p[1]/a')[0].items()[2][1]
                    texto += "Título: %s\nUpvotes: %d\nSubreddits: %s\nLink para os comentários: %s\nLink para thread:  https://www.reddit.com%s\n\n" %(titulo,upvotes,subreddits,comentarios,linkThread)
                except Exception as ee:
                    print(ee)
        except IndexError as ie:
            break
    return texto

def handle(msg):
    pesquisas = msg.split(';')
    for pesquisa in pesquisas:
        a = listar(pesquisa)
        print("%s\n" % a if a != '' else 'nada encontrado com mais de 5000 upvotes para \"%s\"' % pesquisa)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("exemplo de entrada: python3 crawler_parte1.py \"cats;dogs\"")
    else:
        handle("%s" % sys.argv[1])
