# --- SOMMAIRE --- # 
# 2. Extraction et sauvegarde sous csv les données de tous les livres d'une catégorie



# ----- # ---- # ----- # ---- # ----- # ---- # ----- # ---- #
# -- Packages/Modules pré-requis -- #

import requests # pour envoyer des requêtes HTTP via Python
from bs4 import BeautifulSoup # pour faciliter l'extraction des liens de notre page web
import html.parser # pour parser le contenu html
import soupsieve # pour récupérer facilement du contenu html là où il n'y a pas de 'class' ni de 'id'
import csv # pour faciliter le sauvegarde des données sous csv
import random # pour choisir un élément au hasard dans une liste
import os # pour créer un dossier



# ----- # ---- # ----- # ---- # ----- # ---- # ----- # ---- #
# -- 2. Extraction et sauvegarde sous csv les données de tous les livres d'une catégorie choisie automatiquement au hasard -- #

if __name__=="__main__":

        def books_function1():
        
                path = "./categorie_csv/" # -- Création d'un dossier d'une catégorie choisie au hasard contenant les données de tous les livres de cette catégorie -- #
                if path==False:
                        os.mkdir(path)
                else:
                        pass

                def les_livres_d_une_categorie():
                        """ Fonction d'extraction des données de toutes les livres d'une catégorie choisie au hasard """
                        
                        les_urls_de_toutes_les_categories = []

                        les_noms_de_toutes_les_categories = []


                        url_page_d_accueil = 'http://books.toscrape.com/'

                        r1 = requests.get(url_page_d_accueil)

                        if r1.ok:
                        
                                soup1 = BeautifulSoup(r1.content, 'html.parser')
                                
                                categ_urls = soup1.select(".nav > li:nth-child(1) > ul:nth-child(2) > li")
                                
                                for x in categ_urls:  
                                        
                                        a = x.find('a')
                                        
                                        # -- pour obtenir les urls de toutes les catégories, à mettre dans les_urls_de_toutes_les_categories[] -- #
                                        url_de_chaque_catgerie_a_la_page_d_accueil = a['href']
                                        les_urls_de_toutes_les_categories.append('http://books.toscrape.com/' + url_de_chaque_catgerie_a_la_page_d_accueil)
                                        
                                        # -- pour extraire les noms de toutes les catégories, pour les placer dans les_noms_de_toutes_les_categories[] -- #
                                        nom_de_chaque_categorie = a.text.strip()
                                        les_noms_de_toutes_les_categories.append(str(nom_de_chaque_categorie))
                        

                        urls_de_tous_les_livres_dans_toutes_les_categories = []

                        filename = './categorie_csv/une_categorie.csv' # -- la catégorie sera choisie au hasard

                        with open(filename,'w') as f:
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


                                url = random.choice(les_urls_de_toutes_les_categories).replace('index.html', '') # --- un url est choisi au hasard dans la liste 'les_urls_de_toutes_les_categories' -- #

                                r2 = requests.get(url)

                                if r2.ok:
                                                
                                        soup2 = BeautifulSoup(r2.content, 'html.parser')
                                                
                                        next_page_url = soup2.find_all("li", {"class":"next"})

                                        # ---  s'il y a 'next_page_url' sur une page catégorie, cette catégorie a plusieurs pages; autrement, c'est une catégorie à page unique
                                        # ---  On va traiter ici les éléments d'une catégorie choisie au hasard dans le site

                                        if next_page_url: 
                                                
                                                # ---  'nombre_de_page' indique le nombre de page d'une catégorie, alloué à la variable 'i' ci-après 

                                                nombre_de_page_d_une_categorie = soup2.find('li', {'class': 'current'})
                                                
                                                nombre_de_page = int(nombre_de_page_d_une_categorie.text.strip()[-1])

                                                i = 1
                                                while i <= nombre_de_page:
                                                
                                                        # --- on va traiter ici les éléments de chaque catégorie en fonction de leur nombre de page

                                                        url_de_categ_avec_plusieurs_pages = url + 'page-' + str(i) + '.html'               
                                                        i += 1

                                                        response3 = requests.get(url_de_categ_avec_plusieurs_pages)
                                                        
                                                        soup3 = BeautifulSoup(response3.content, 'html.parser')
                                                        
                                                        book_urls3 = soup3.find_all("article", {"class":"product_pod"})
                                                        
                                                        for book_url3 in book_urls3:  
                                                                a3 = book_url3.find('a')
                                                                suffixe_url_d_un_livre_avec_categ_a_plusieurs_pages = a3['href'].replace('../../../', '')
                                                                
                                                                url_d_un_livre_avec_categ_a_plusieurs_pages = 'http://books.toscrape.com/catalogue/' + suffixe_url_d_un_livre_avec_categ_a_plusieurs_pages
                                                                
                                                                urls_de_tous_les_livres_dans_toutes_les_categories.append(url_d_un_livre_avec_categ_a_plusieurs_pages)

                                                                # --- on va scraper les données sur chaque page-livre
                                                                
                                                                response33 = requests.get(url_d_un_livre_avec_categ_a_plusieurs_pages)
                                                                
                                                                soup33 = BeautifulSoup(response33.content, 'html.parser')

                                                                prodUrl3 = url_d_un_livre_avec_categ_a_plusieurs_pages # pour obtenir l'url de la page produit en cours

                                                                product_information3 = []  # pour obtenir les 'product_information' de chaque livre 

                                                                tds3 = soup33.find_all('td') 
                                                                
                                                                for td in tds3:
                                                                        product_information3.append(td.text) # le lien pour scraper tous les 'td'
                                                                
                                                                upc3 = product_information3[0] # pour obtenir l'UPC de chaque livre
                                                                
                                                                title3 = soup33.find('h1').text.replace(",", " -") # pour obtenir le titre de chaque livre
                                                                
                                                                prixTtc3 = product_information3[2].replace("Â", " ") # pour obtenir le prix ttc de chaque livre

                                                                prixHt3 = product_information3[3].replace("Â", " ") # pour afficher le prix ht de chaque livre  
                                                                
                                                                numberAvail3 = product_information3[5].replace("In stock (", " ").replace(" available)", " ") # pour obtenir la quantité disponible de chaque livre
                                                                
                                                                product_desc3 = soup33.select('.product_page > p') # Pour extraire la description de chaque livre
                                                                desc3 = str(product_desc3).replace('<p>', ' ').replace('</p>', ' ').replace('[', '"').replace(']', '"')

                                                                category3 = soup33.find("ul", {"class":"breadcrumb"}).find_all('li')[2] # Pour obtenir la categorie de chaque livre
                                                                catname3 = BeautifulSoup(str(category3).replace("\n", " "), 'html.parser').get_text().encode("utf-8")
                                                                categ3 = str(catname3).replace("'", " ").replace('b', '').strip()
                                                                
                                                                reviews3 = [] # Pour obtenir le review_rating de chaque livre 
                                                                review_rating3 = soup33.find_all('p', {'class': 'star-rating'})
                                                                for p in review_rating3:
                                                                        link3 = p['class'][1]
                                                                        reviews3.append(link3)
                                                                reviewR3 = reviews3[0].replace("['star-rating',", " ").replace("]", "").replace("'", " ")
                                                                
                                                                imageurl3 = ('http://books.toscrape.com/' + str(soup33.find('img')['src'].replace('../../', ''))) # Pour obtenir image_url
                                                                
                                                                data_livre = (  # --- contenu du csv 
                                                                        str(prodUrl3),
                                                                        str(upc3),
                                                                        str(title3),
                                                                        str(prixTtc3),
                                                                        str(prixHt3),
                                                                        str(numberAvail3),
                                                                        str(desc3),
                                                                        str(categ3),
                                                                        str(reviewR3),
                                                                        str(imageurl3)
                                                                )
                                                                
                                                                csv_writer.writerow(data_livre)
                                                        
                                        
                                        # --- 2. Ici on va traiter chaque catégorie à page unique -- # 
                                
                                        else:
                                                
                                                book_urls_avec_categ_a_page_unique = soup2.find_all("article", {"class":"product_pod"})
                                                
                                                for book_url4 in book_urls_avec_categ_a_page_unique:
                                                        a4 = book_url4.find('a')
                                                        suffixe_url_d_un_livre_avec_categ_a_page_unique = a4['href'].replace('../../../', '')
                                                        
                                                        url_d_un_livre_avec_categ_a_page_unique = 'http://books.toscrape.com/catalogue/' + suffixe_url_d_un_livre_avec_categ_a_page_unique
                                                        
                                                        urls_de_tous_les_livres_dans_toutes_les_categories.append(url_d_un_livre_avec_categ_a_page_unique)
                                                        
                                                        # --- on va traiter chaque livre de cette catégorie à page unique

                                                        response44 = requests.get(url_d_un_livre_avec_categ_a_page_unique)
                                                        
                                                        soup44 = BeautifulSoup(response44.content, 'html.parser')

                                                        prodUrl4 = url_d_un_livre_avec_categ_a_page_unique # pour obtenir l'url de la page produit en cours

                                                        product_information4 = []  # pour obtenir les 'product_information' de chaque livre

                                                        tds4 = soup44.find_all('td') 
                                                        for td in tds4:
                                                                product_information4.append(td.text) # le lien pour scraper tous les 'td'
                                                        
                                                        upc4 = product_information4[0] # pour obtenir l'UPC de chaque livre
                                                        
                                                        title4 = soup44.find('h1').text.replace(",", " -") # pour obtenir le titre de chaque livre
                                                        
                                                        prixTtc4 = product_information4[2].replace("Â", " ") # pour obtenir le prix ttc de chaque livre

                                                        prixHt4 = product_information4[3].replace("Â", " ") # pour afficher le prix ht de chaque livre  
                                                        
                                                        numberAvail4 = product_information4[5].replace("In stock (", " ").replace(" available)", " ") # pour obtenir la quantité disponible de chaque livre
                                                        
                                                        product_desc4 = soup44.select('.product_page > p') # Pour extraire la description de chaque livre 
                                                        desc4 = str(product_desc4).replace('<p>', ' ').replace('</p>', ' ').replace('[', '"').replace(']', '"')
                                                
                                                        category4 = soup44.find("ul", {"class":"breadcrumb"}).find_all('li')[2] # Pour obtenir la categorie de chaque livre
                                                        catname4 = BeautifulSoup(str(category4).replace("\n", " "), 'html.parser').get_text().encode("utf-8")
                                                        categ4 = str(catname4).replace("'", " ").replace('b', '').strip()
                                                        
                                                        
                                                        reviews4 = [] # Pour obtenir le review_rating de chaque livre 
                                                        review_rating4 = soup44.find_all('p', {'class': 'star-rating'})
                                                        for p in review_rating4:
                                                                link4 = p['class'][1]
                                                                reviews4.append(link4)
                                                        reviewR4 = reviews4[0].replace("['star-rating',", " ").replace("]", "").replace("'", " ")
                                                        
                                                        imageurl4 = ('http://books.toscrape.com/' + str(soup44.find('img')['src'].replace('../../', ''))) # Pour obtenir image_url
                                                        
                                                        data_livre = ( # --- contenu du csv 
                                                                str(prodUrl4),
                                                                str(upc4),
                                                                str(title4),
                                                                str(prixTtc4),
                                                                str(prixHt4),
                                                                str(numberAvail4),
                                                                str(desc4),
                                                                str(categ4),
                                                                str(reviewR4),
                                                                str(imageurl4)
                                                        )
                                                        
                                                        csv_writer.writerow(data_livre)
                                        
                les_livres_d_une_categorie()  # -- Veuillez retirer le commentaire au début de cette ligne pour activer le script -- #

        books_function1()
        
else:

        def books_function2():
        
                path = "./categorie_csv/" # -- Création d'un dossier d'une catégorie choisie au hasard contenant les données de tous les livres de cette catégorie -- #
                if path==False:
                        os.mkdir(path)
                else:
                        pass

                def les_livres_d_une_categorie():
                        """ Fonction d'extraction des données de toutes les livres d'une catégorie choisie au hasard """
                        
                        les_urls_de_toutes_les_categories = []

                        les_noms_de_toutes_les_categories = []


                        url_page_d_accueil = 'http://books.toscrape.com/'

                        r1 = requests.get(url_page_d_accueil)

                        if r1.ok:
                        
                                soup1 = BeautifulSoup(r1.content, 'html.parser')
                                
                                categ_urls = soup1.select(".nav > li:nth-child(1) > ul:nth-child(2) > li")
                                
                                for x in categ_urls:  
                                        
                                        a = x.find('a')
                                        
                                        # -- pour obtenir les urls de toutes les catégories, à mettre dans les_urls_de_toutes_les_categories[] -- #
                                        url_de_chaque_catgerie_a_la_page_d_accueil = a['href']
                                        les_urls_de_toutes_les_categories.append('http://books.toscrape.com/' + url_de_chaque_catgerie_a_la_page_d_accueil)
                                        
                                        # -- pour extraire les noms de toutes les catégories, pour les placer dans les_noms_de_toutes_les_categories[] -- #
                                        nom_de_chaque_categorie = a.text.strip()
                                        les_noms_de_toutes_les_categories.append(str(nom_de_chaque_categorie))
                        

                        urls_de_tous_les_livres_dans_toutes_les_categories = []

                        filename = './categorie_csv/une_categorie.csv' # -- la catégorie sera choisie au hasard

                        with open(filename,'w') as f:
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


                                url = random.choice(les_urls_de_toutes_les_categories).replace('index.html', '') # --- un url est choisi au hasard dans la liste 'les_urls_de_toutes_les_categories' -- #

                                r2 = requests.get(url)

                                if r2.ok:
                                                
                                        soup2 = BeautifulSoup(r2.content, 'html.parser')
                                                
                                        next_page_url = soup2.find_all("li", {"class":"next"})

                                        # ---  s'il y a 'next_page_url' sur une page catégorie, cette catégorie a plusieurs pages; autrement, c'est une catégorie à page unique
                                        # ---  On va traiter ici les éléments d'une catégorie choisie au hasard dans le site

                                        if next_page_url: 
                                                
                                                # ---  'nombre_de_page' indique le nombre de page d'une catégorie, alloué à la variable 'i' ci-après 

                                                nombre_de_page_d_une_categorie = soup2.find('li', {'class': 'current'})
                                                
                                                nombre_de_page = int(nombre_de_page_d_une_categorie.text.strip()[-1])

                                                i = 1
                                                while i <= nombre_de_page:
                                                
                                                        # --- on va traiter ici les éléments de chaque catégorie en fonction de leur nombre de page

                                                        url_de_categ_avec_plusieurs_pages = url + 'page-' + str(i) + '.html'               
                                                        i += 1

                                                        response3 = requests.get(url_de_categ_avec_plusieurs_pages)
                                                        
                                                        soup3 = BeautifulSoup(response3.content, 'html.parser')
                                                        
                                                        book_urls3 = soup3.find_all("article", {"class":"product_pod"})
                                                        
                                                        for book_url3 in book_urls3:  
                                                                a3 = book_url3.find('a')
                                                                suffixe_url_d_un_livre_avec_categ_a_plusieurs_pages = a3['href'].replace('../../../', '')
                                                                
                                                                url_d_un_livre_avec_categ_a_plusieurs_pages = 'http://books.toscrape.com/catalogue/' + suffixe_url_d_un_livre_avec_categ_a_plusieurs_pages
                                                                
                                                                urls_de_tous_les_livres_dans_toutes_les_categories.append(url_d_un_livre_avec_categ_a_plusieurs_pages)

                                                                # --- on va scraper les données sur chaque page-livre
                                                                
                                                                response33 = requests.get(url_d_un_livre_avec_categ_a_plusieurs_pages)
                                                                
                                                                soup33 = BeautifulSoup(response33.content, 'html.parser')

                                                                prodUrl3 = url_d_un_livre_avec_categ_a_plusieurs_pages # pour obtenir l'url de la page produit en cours

                                                                product_information3 = []  # pour obtenir les 'product_information' de chaque livre 

                                                                tds3 = soup33.find_all('td') 
                                                                
                                                                for td in tds3:
                                                                        product_information3.append(td.text) # le lien pour scraper tous les 'td'
                                                                
                                                                upc3 = product_information3[0] # pour obtenir l'UPC de chaque livre
                                                                
                                                                title3 = soup33.find('h1').text.replace(",", " -") # pour obtenir le titre de chaque livre
                                                                
                                                                prixTtc3 = product_information3[2].replace("Â", " ") # pour obtenir le prix ttc de chaque livre

                                                                prixHt3 = product_information3[3].replace("Â", " ") # pour afficher le prix ht de chaque livre  
                                                                
                                                                numberAvail3 = product_information3[5].replace("In stock (", " ").replace(" available)", " ") # pour obtenir la quantité disponible de chaque livre
                                                                
                                                                product_desc3 = soup33.select('.product_page > p') # Pour extraire la description de chaque livre
                                                                desc3 = str(product_desc3).replace('<p>', ' ').replace('</p>', ' ').replace('[', '"').replace(']', '"')

                                                                category3 = soup33.find("ul", {"class":"breadcrumb"}).find_all('li')[2] # Pour obtenir la categorie de chaque livre
                                                                catname3 = BeautifulSoup(str(category3).replace("\n", " "), 'html.parser').get_text().encode("utf-8")
                                                                categ3 = str(catname3).replace("'", " ").replace('b', '').strip()
                                                                
                                                                reviews3 = [] # Pour obtenir le review_rating de chaque livre 
                                                                review_rating3 = soup33.find_all('p', {'class': 'star-rating'})
                                                                for p in review_rating3:
                                                                        link3 = p['class'][1]
                                                                        reviews3.append(link3)
                                                                reviewR3 = reviews3[0].replace("['star-rating',", " ").replace("]", "").replace("'", " ")
                                                                
                                                                imageurl3 = ('http://books.toscrape.com/' + str(soup33.find('img')['src'].replace('../../', ''))) # Pour obtenir image_url
                                                                
                                                                data_livre = (  # --- contenu du csv 
                                                                        str(prodUrl3),
                                                                        str(upc3),
                                                                        str(title3),
                                                                        str(prixTtc3),
                                                                        str(prixHt3),
                                                                        str(numberAvail3),
                                                                        str(desc3),
                                                                        str(categ3),
                                                                        str(reviewR3),
                                                                        str(imageurl3)
                                                                )
                                                                
                                                                csv_writer.writerow(data_livre)
                                                        
                                        
                                        # --- 2. Ici on va traiter chaque catégorie à page unique -- # 
                                
                                        else:
                                                
                                                book_urls_avec_categ_a_page_unique = soup2.find_all("article", {"class":"product_pod"})
                                                
                                                for book_url4 in book_urls_avec_categ_a_page_unique:
                                                        a4 = book_url4.find('a')
                                                        suffixe_url_d_un_livre_avec_categ_a_page_unique = a4['href'].replace('../../../', '')
                                                        
                                                        url_d_un_livre_avec_categ_a_page_unique = 'http://books.toscrape.com/catalogue/' + suffixe_url_d_un_livre_avec_categ_a_page_unique
                                                        
                                                        urls_de_tous_les_livres_dans_toutes_les_categories.append(url_d_un_livre_avec_categ_a_page_unique)
                                                        
                                                        # --- on va traiter chaque livre de cette catégorie à page unique

                                                        response44 = requests.get(url_d_un_livre_avec_categ_a_page_unique)
                                                        
                                                        soup44 = BeautifulSoup(response44.content, 'html.parser')

                                                        prodUrl4 = url_d_un_livre_avec_categ_a_page_unique # pour obtenir l'url de la page produit en cours

                                                        product_information4 = []  # pour obtenir les 'product_information' de chaque livre

                                                        tds4 = soup44.find_all('td') 
                                                        for td in tds4:
                                                                product_information4.append(td.text) # le lien pour scraper tous les 'td'
                                                        
                                                        upc4 = product_information4[0] # pour obtenir l'UPC de chaque livre
                                                        
                                                        title4 = soup44.find('h1').text.replace(",", " -") # pour obtenir le titre de chaque livre
                                                        
                                                        prixTtc4 = product_information4[2].replace("Â", " ") # pour obtenir le prix ttc de chaque livre

                                                        prixHt4 = product_information4[3].replace("Â", " ") # pour afficher le prix ht de chaque livre  
                                                        
                                                        numberAvail4 = product_information4[5].replace("In stock (", " ").replace(" available)", " ") # pour obtenir la quantité disponible de chaque livre
                                                        
                                                        product_desc4 = soup44.select('.product_page > p') # Pour extraire la description de chaque livre 
                                                        desc4 = str(product_desc4).replace('<p>', ' ').replace('</p>', ' ').replace('[', '"').replace(']', '"')
                                                
                                                        category4 = soup44.find("ul", {"class":"breadcrumb"}).find_all('li')[2] # Pour obtenir la categorie de chaque livre
                                                        catname4 = BeautifulSoup(str(category4).replace("\n", " "), 'html.parser').get_text().encode("utf-8")
                                                        categ4 = str(catname4).replace("'", " ").replace('b', '').strip()
                                                        
                                                        
                                                        reviews4 = [] # Pour obtenir le review_rating de chaque livre 
                                                        review_rating4 = soup44.find_all('p', {'class': 'star-rating'})
                                                        for p in review_rating4:
                                                                link4 = p['class'][1]
                                                                reviews4.append(link4)
                                                        reviewR4 = reviews4[0].replace("['star-rating',", " ").replace("]", "").replace("'", " ")
                                                        
                                                        imageurl4 = ('http://books.toscrape.com/' + str(soup44.find('img')['src'].replace('../../', ''))) # Pour obtenir image_url
                                                        
                                                        data_livre = ( # --- contenu du csv 
                                                                str(prodUrl4),
                                                                str(upc4),
                                                                str(title4),
                                                                str(prixTtc4),
                                                                str(prixHt4),
                                                                str(numberAvail4),
                                                                str(desc4),
                                                                str(categ4),
                                                                str(reviewR4),
                                                                str(imageurl4)
                                                        )
                                                        
                                                        csv_writer.writerow(data_livre)
                                        
                les_livres_d_une_categorie()  # -- Veuillez retirer le commentaire au début de cette ligne pour activer le script -- #
                
                print("C'est fini. Veuillez vérifier la mise à jour du dossier: " + str(path.replace("./", "")))
