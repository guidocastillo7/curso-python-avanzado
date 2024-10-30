import logging
import requests
from bs4 import BeautifulSoup
from prefect import task

LINKEDIN_URL = 'https://www.linkedin.com/jobs/search/?keywords=#&position=1&pageNum=0'


#@task(name="Obtener ofertas laborales")
def get_offers(skill):
    url = requests.get(LINKEDIN_URL.replace('#',skill))
    
    if(url.status_code == 200):
        print(f"EXTRACCIÓN DE DATA...")
        html = BeautifulSoup(url.text,'html.parser')
        dataOfertas = html.find('ul',{'class':'jobs-search__results-list'})
        listaOfertas = dataOfertas.find_all('li')
        resultadoOfertas = []
        for oferta in listaOfertas:
            titulo = oferta.find('h3',{'class':'base-search-card__title'})
            empresa = oferta.find('span',{'class':'job-search-card__location'})
            urlOferta = oferta.find('a',{'class':'base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]'})
            dicOferta = {
                'puesto':titulo.get_text().strip(),
                'ubicacion':empresa.get_text().strip(),
                'url': urlOferta['href'].strip()
            }
            resultadoOfertas.append(dicOferta)
        return resultadoOfertas
		
    else:
        print("error " + str(url.status_code))