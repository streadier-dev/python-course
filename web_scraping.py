import requests
from bs4 import BeautifulSoup
import urllib.request
import os.path
from os import path


def run():
    for i in range(1, 6):
        response = requests.get('https://xkcd.com/{}'.format(i))
        soup = BeautifulSoup(response.content, 'html.parser')
        image_container = soup.find(id='comic')

        image_url = image_container.find('img')['src']
        image_name = image_url.split('/')[-1]
        #print("Is it Directory?" + str(path.isdir(r"C:\Users\gabriel\python\python-project\imagenes")))
        directory = os.path.isdir(r"C:\Users\gabriel\python\python-project\imagenes")
        if directory == True:
            filepath = os.path.join(r"C:\Users\gabriel\python\python-project\imagenes",image_name)
            print('Descargando la imagen {}'.format(image_name, filepath))
            urllib.request.urlretrieve('https:{}'.format(image_url), filepath)
        else:
            print('Directorio no creado, se creara un directorio \images en la carpeta de ejecuccion del programa')
            os.mkdir(r"C:\Users\gabriel\python\python-project\imagenes")

if __name__ == '__main__':
    run()
