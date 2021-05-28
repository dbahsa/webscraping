# --- SOMMAIRE --- # 
# 4. Extraction et sauvegarde de toutes les images de chaque livre un dossier images



# ----- # ---- # ----- # ---- # ----- # ---- # ----- # ---- #
# -- Packages/Modules pré-requis -- #

import requests # pour envoyer des requêtes HTTP via Python
from bs4 import BeautifulSoup # pour faciliter l'extraction des liens de notre page web
import html.parser # pour parser le contenu html
import soupsieve # pour récupérer facilement du contenu html là où il n'y a pas de 'class' ni de 'id'
import csv # pour faciliter le sauvegarde des données sous csv
import random # pour choisir un élément au hasard dans une liste
import shutil # pour faciliter la sauvegarde des images
import os # pour créer un dossier



# ----- # ---- # ----- # ---- # ----- # ---- # ----- # ---- #
# -- 4. Extraction et sauvegarde de toutes les images de chaque livre dans un dossier image -- #

if __name__=="__main__":

        def image_function1():

                path = "./images/" # -- Création d'un dossier pour contenir toutes les images de page-produit du site -- #
                if path==False:
                        os.mkdir(path)
                else:
                        pass

                def les_images_du_site():
                        """ Fonction pour télécharger et sauvegarder toutes les images du site """

                        les_noms_de_toutes_les_categories = [] # -- pour récupérer le nmbre total des catégories (ici=50) -- #

                        url_page_d_accueil = 'http://books.toscrape.com/'

                        r1 = requests.get(url_page_d_accueil)

                        if r1.ok:
                        
                                soup_image = BeautifulSoup(r1.content, 'html.parser')
                                
                                categ_urls = soup_image.select(".nav > li:nth-child(1) > ul:nth-child(2) > li")
                                
                                for x in categ_urls:  
                                        a = x.find('a')
                                        nom_de_chaque_categorie = a.text.strip()  # -- pour extraire les noms de toutes les catégories -- #
                                        les_noms_de_toutes_les_categories.append(str(nom_de_chaque_categorie))



                                image_urls = [] # -- liste comprenant tous les urls des images du site -- #

                                for i in range(1, 1 + len(les_noms_de_toutes_les_categories)):
                                        
                                        url = 'http://books.toscrape.com/catalogue/page-' + str(i) + '.html'
                                        
                                        response = requests.get(url)

                                        photo = BeautifulSoup(response.content, 'html.parser')
                                        
                                        image_url = photo.find_all('img')
                                        for img in image_url:  
                                                link = img['src']
                                                image_urls.append('http://books.toscrape.com/' + link)

                                
                                with open('./images/imageUrls.txt', 'w') as file: # -- 'imageUrls.txt' créé dans un sous-dossier, 'images', pour éviter de télécharger toutes les images dans le dossier principal -- #
                                        for link in image_urls: 
                                                file.write(link + '\n')
                                
                                
                                with open('./images/imageUrls.txt', 'r') as inf: # -- lancer l'extraction des photos de chaque couverture des livres -- # 

                                        for row in inf:
                                                
                                                image_url = row.strip()
                                                
                                                imageName = image_url.split('/')[-1]

                                                r_photo = requests.get(image_url,stream=True)

                                                r_photo.raw.decode_content = True

                                                with open(f'./images/{imageName}', 'wb') as f: # -- sauvegarde de chaque image  -- #

                                                        shutil.copyfileobj(r_photo.raw,f)

                les_images_du_site()  # -- Veuillez retirer le commentaire au début de cette ligne pour activer le script -- #

        image_function1()

else:
        def image_function2():

                path = "./images/" # -- Création d'un dossier pour contenir toutes les images de page-produit du site -- #
                if path==False:
                        os.mkdir(path)
                else:
                        pass

                def les_images_du_site():
                        """ Fonction pour télécharger et sauvegarder toutes les images du site """

                        les_noms_de_toutes_les_categories = [] # -- pour récupérer le nmbre total des catégories (ici=50) -- #

                        url_page_d_accueil = 'http://books.toscrape.com/'

                        r1 = requests.get(url_page_d_accueil)

                        if r1.ok:
                        
                                soup_image = BeautifulSoup(r1.content, 'html.parser')
                                
                                categ_urls = soup_image.select(".nav > li:nth-child(1) > ul:nth-child(2) > li")
                                
                                for x in categ_urls:  
                                        a = x.find('a')
                                        nom_de_chaque_categorie = a.text.strip()  # -- pour extraire les noms de toutes les catégories -- #
                                        les_noms_de_toutes_les_categories.append(str(nom_de_chaque_categorie))



                                image_urls = [] # -- liste comprenant tous les urls des images du site -- #

                                for i in range(1, 1 + len(les_noms_de_toutes_les_categories)):
                                        
                                        url = 'http://books.toscrape.com/catalogue/page-' + str(i) + '.html'
                                        
                                        response = requests.get(url)

                                        photo = BeautifulSoup(response.content, 'html.parser')
                                        
                                        image_url = photo.find_all('img')
                                        for img in image_url:  
                                                link = img['src']
                                                image_urls.append('http://books.toscrape.com/' + link)

                                
                                with open('./images/imageUrls.txt', 'w') as file: # -- 'imageUrls.txt' créé dans un sous-dossier, 'images', pour éviter de télécharger toutes les images dans le dossier principal -- #
                                        for link in image_urls: 
                                                file.write(link + '\n')
                                
                                
                                with open('./images/imageUrls.txt', 'r') as inf: # -- lancer l'extraction des photos de chaque couverture des livres -- # 

                                        for row in inf:
                                                
                                                image_url = row.strip()
                                                
                                                imageName = image_url.split('/')[-1]

                                                r_photo = requests.get(image_url,stream=True)

                                                r_photo.raw.decode_content = True

                                                with open(f'./images/{imageName}', 'wb') as f: # -- sauvegarde de chaque image  -- #

                                                        shutil.copyfileobj(r_photo.raw,f)

                les_images_du_site()  # -- Veuillez retirer le commentaire au début de cette ligne pour activer le script -- #

                print("C'est fini. Veuillez vérifier la mise à jour du dossier: " + str(path.replace("./", "").replace("/", "")))
