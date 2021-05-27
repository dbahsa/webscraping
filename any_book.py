# --- SOMMAIRE --- # 
# 1. Extraction et sauvegarde sous csv les données d'un livre



# ----- # ---- # ----- # ---- # ----- # ---- # ----- # ---- #
# -- Packages/Modules pré-requis -- #

import requests # pour envoyer des requêtes HTTP via Python
from bs4 import BeautifulSoup # pour faciliter l'extraction des liens de notre page web
import html.parser # pour parser le contenu html
import soupsieve # pour récupérer facilement du contenu html là où il n'y a pas de 'class' ni de 'id'
import csv # pour faciliter le sauvegarde des données sous csv
import random # pour choisir un élément au hasard dans une liste
import os, sys # pour créer un dossier



# ----- # ---- # ----- # ---- # ----- # ---- # ----- # ---- #
# -- 1. Tout le script pour obtenir les données d'un livre choisi automatiquement au hasard sur la page d'accueil  -- #

if __name__=="__main__":

    path = "./livre_csv/" # -- Création du dossier contenant le fichier csv d'un livre -- #
    if path==False:
        os.mkdir(path)
    else:
        pass

    def info_d_un_livre():
            """ Fonction pour récupérer et sauvegarder dans un fichier csv les données d'un livre choisi au hasard """

            with open('./livre_csv/livre.csv','w') as f:  # -- les données du 1er livre sont enregistrées dans 'livre.csv' dans le doccier 'livre_csv' --#
                    csv_writer = csv.writer(f, lineterminator='\n')
                    header = (
                    'product_page_url', 
                    'universal_product_code', 
                    'title', 
                    'price_including_tax', 
                    'price_excluding_tax', 
                    'number_available', 
                    'product_description', 
                    'category', 
                    'review_rating', 
                    'image_url'
                    )      
                    csv_writer.writerow(header) # -- pour ajouter l'en-tête en haut


                    url_page_d_accueil = 'http://books.toscrape.com/' # -- la page d'accueil -- #

                    r1 = requests.get(url_page_d_accueil)

                    if r1.ok:
                    
                            page_d_accueil = BeautifulSoup(r1.content, 'html.parser')

                            
                            livre_au_hasard = [] # -- la liste pour aider à choisir un livre au hasard sur la page d'accueil -- #
                            livres_au_pif = page_d_accueil.find_all("article", {"class":"product_pod"})
                            for livre in livres_au_pif:
                                    livre_au_hasard.append(livre.a['href'])
                            
                            book_url = url_page_d_accueil + random.choice(livre_au_hasard) # -- on va scraper un livre trouvé au hasard sur la page d'accueil -- #
                            
                            r11 =  requests.get(book_url)

                            soup11 = BeautifulSoup(r11.content, 'html.parser')

                            prodUrl = book_url # pour afficher l'url de page livre
                            
                            product_information = []  # la liste qui recupère les infos d'un livre (upc, prix, etc.)               
                            tds = soup11.find_all('td') 
                            for td in tds:
                                    product_information.append(td.text)

                            upc = product_information[0]  # pour extraire l'UPC de chaque livre
                            
                            title = soup11.find('h1').text.replace(",", " -") # pour afficher le titre d'un livre 
                            
                            prixTtc = product_information[2].replace("Â", " ") # pour afficher le prix ttc d'un livre
                            
                            prixHt = product_information[3].replace("Â", " ") # pour afficher le prix ht d'un livre
                            
                            numberAvail = product_information[5].replace("In stock (", " ").replace(" available)", " ") # pour obtenir la quantité disponible d'un livre
                            
                            product_description = soup11.select('.product_page > p') # Pour extraire la description  d'un livre
                            desc = str(product_description).replace('"', '“').replace('<p>', ' ').replace('</p>', ' ').replace('[', '"').replace(']', '"')
                            
                            category = soup11.find("ul", {"class":"breadcrumb"}).find_all('li')[2] # Pour afficher la categorie  d'un livre
                            catname = BeautifulSoup(str(category).replace("\n", " "), 'html.parser').get_text().encode("utf-8")
                            categ = str(catname).replace("'", " ").replace('b', '')
                            
                            reviews = []   # la liste pour récupérer les évalutions client
                            review_rating = soup11.find_all('p', {'class': 'star-rating'})
                            for p in review_rating:
                                    link = p['class'][1]
                                    reviews.append(link)
                            reviewR = reviews[0].replace("['star-rating',", " ").replace("]", "").replace("'", " ")
                            
                            imageurl = ('http://books.toscrape.com/' + str(soup11.find('img')['src'].replace('../../', ''))) # Pour obtenir image_url

                            data_livre = (  # --- contenu du csv 
                                    str(prodUrl),
                                    str(upc),
                                    str(title),
                                    str(prixTtc),
                                    str(prixHt),
                                    str(numberAvail),
                                    str(desc),
                                    str(categ),
                                    str(reviewR),
                                    str(imageurl)
                                )
                            
                            csv_writer.writerow(data_livre)
                    
    info_d_un_livre()
