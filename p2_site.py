# --- SOMMAIRE --- #

# 1. Demandes du client
# 2. Packages/Modules pré-requis
# 3. Script pour récupérer les urls des livres d'une catégorie pour les mettre dans un fichier csv
# 4. Script pour extraire et sauvegarde en csv toutes les données des ouvrages d'une catégorie
# 5. Conclusion

# ----- # ---- # ----- # ---- # ----- # ---- # ----- # ---- #


# 1. Demandes du client:

"""

3. Sur la page d'acceuil de 'books.toscrape.com':
        3a. Extraire toutes les catégories de livres disponibles;
        3b. Extraire les informations produit de tous les livres appartenant à toutes les différentes catégories;
        3c. Ecrire les données dans "un fichier CSV distinct pour chaque catégorie" de livres;
        3d. Télécharger dans un dossier 'images' les images de chaque livre dans chaque catégorie.

"""

# ----- # ---- # ----- # ---- # ----- # ---- # ----- # ---- #


# 2. Packages/Modules pré-requis:

import requests # pour envoyer des requêtes HTTP via Python
from bs4 import BeautifulSoup # pour faciliter l'extraction des liens de notre page web
import html.parser # pour parser le contenu html
import soupsieve # pour récupérer facilement du contenu html là où il n'y a pas de 'class' ni de 'id'
import time # pour mettre un delai en sec entre chaque boucle pour éviter la procédure d'être bloqué par le serveur du site d'extraction


# ----- # ---- # ----- # ---- # ----- # ---- # ----- # ---- #


# 3a. Script pour Extraire toutes les catégories de livres disponibles:

"""

Info catégories: 
    - Quantité: 50
    - Scrapées à partir: http://books.toscrape.com/
    - Le fichier contenant les urls des catégories: categsUrls.txt

"""


"""

links = []
url = 'http://books.toscrape.com/'
response = requests.get(url)

if response.status_code != 200:
    print('Le site est inaccessible.  Veuillez réessayer plus tard')

else:
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Pour afficher toutes les catégories (#.nav > li:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > a)
    
    # Pour afficher l'url de chaque catégorie
    categ_urls = soup.select(".nav > li:nth-child(1) > ul:nth-child(2) > li")
    for categ_url in categ_urls:  
        a = categ_url.find('a')
        link = a['href'] #.replace('../../../', '')
        links.append('http://books.toscrape.com/' + link)
            
    time.sleep(2) # pour ralentir le boucle de 2sec pour éventuellement éviter que l'extraction des données soit bloquée

with open('categsUrls.txt', 'w') as file: # categsUrls.txt contient les urls de chaque catégorie du site
    for link in links: # nous allons utiliser categsUrls.txt pour scraper les données de chaque cchaque catégorie du site
        file.write(link + '\n')

"""



# ----- # ---- # ----- # ---- # ----- # ---- # ----- # ---- #


# 3b. Script pour extraire les informations produit de tous les livres appartenant à toutes les différentes catégories:
    # 3b.1. Extractiion et sauvegarde dans 'allBooksUrls.txt' de tous les urls de tous les livres à partir de la page d'accueil;
    # 3b.2. Sauvegarde dans 'allBooksUrls.csv' des données de tous les livres du site
    

""" 3b.1.

links = []

for i in range(1, 51):
    url = 'http://books.toscrape.com/catalogue/page-' + str(i) + '.html'
    response = requests.get(url)

    if response.status_code != 200:
        print("Le site est inaccessible.  Veuillez réessayer plus tard")
    else:
        soup = BeautifulSoup(response.text, 'html.parser')
        # print('Page: ' + str(i)) # pour vérifier si le nombre de page où le scraping est effectué est bien correct; ici = 50

        # Pour afficher l'url de chaque livre
        book_urls = soup.find_all("article", {"class":"product_pod"})
        for book_url in book_urls:  
            a = book_url.find('a')
            link = a['href'].replace('../../../', '')
            links.append('http://books.toscrape.com/catalogue/' + link)
        time.sleep(1) # pour ralentir le boucle de 1sec pour éventuellement éviter que l'extraction des données soit bloquée

# print(len(links)) # pour verifier le nombre total des livres; ici = 1000

with open('allBooksUrls.txt', 'w') as file: # 'allBooksUrls.txt' contient les urls de tous les livres peu importe leur catégorie
    for link in links: # ensuite 'allBooksUrls.txt' sera utilisé scraper les données de chaque livre de toutes les catégories
        file.write(link + '\n')

"""


""" 3b.2.

with open('allBooksUrls.txt', 'r') as inf: # 'allBooksUrls.txt' contient les urls tous les livres vendus sur le site
    with open('allBooksUrls.csv', 'w') as outf: # 'allBooksUrls.csv' va contenir les données de tous les livres dans toutes les catégories
        # outf.write(): pour créer l'en-tête de 'allBooksUrls.csv'
        outf.write('product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url\n')
        for row in inf: 
            product_page_url = row.strip()

            response = requests.get(product_page_url)

            if response.status_code != 200:
                print("Le site est inaccessible.  Veuillez réessayer plus tard")
            else:

                soup = BeautifulSoup(response.text, 'html.parser')

                # pour afficher l'url de la page produit en cours de traitement
                prodUrl = product_page_url
                print(prodUrl)
                
                # pour extraire les carateritiques de chaque livre 
                links = []  
                tds = soup.find_all('td') 
                for td in tds:
                    links.append(td.text) # le lien pour scraper tous les 'td'
                
                # pour afficher l'UPC de chaque livre
                upc = links[0]
                print(upc)

                # pour afficher le titre de chaque livre  
                title = soup.find('h1')
                titre = title.text.replace(",", " -")
                print(titre)

                # pour afficher le prix ttc de chaque livre 
                prixTtc = links[2].replace("Â", " ")
                print(prixTtc)

                # pour afficher le prix ht de chaque livre 
                prixHt = links[3].replace("Â", " ")
                print(prixHt)

                # pour obtenir la quantité disponible de chaque livre 
                numberAvail = links[5].replace("In stock (", " ").replace(" available)", " ")
                print(numberAvail)

                # Pour extraire la description de produit
                product_description = soup.select('.product_page > p')
                desc = str(product_description).replace('"', '“').replace('<p>', ' ').replace('</p>', ' ').replace('[', '""').replace(']', '""')
                print(desc)

                # Pour afficher la 'category'
                category = soup.find("ul", {"class":"breadcrumb"}).find_all('li')[2]
                catname = BeautifulSoup(str(category).replace("\n", " "), 'html.parser').get_text().encode("utf-8")
                categ = str(catname).replace("'", " ").replace('b', '')
                print(categ)

                # Pour afficher review_rating
                links = []
                review_rating = soup.find_all('p', {'class': 'star-rating'})
                for p in review_rating:
                    link = p['class'][1]
                    links.append(link)
                reviewR = links[0].replace("['star-rating',", " ").replace("]", "").replace("'", " ")
                print(reviewR) 

                # Pour afficher image_url
                links = []
                image_url = soup.find_all('img')
                for image in image_url:  
                    link = image['src']
                    links.append('http://books.toscrape.com/' + link)
                imageurl = links[0]
                print(imageurl)  # print(links[0]) # imprime sans l'en-tête

                outf.write(str(prodUrl) + ' , ' + str(upc) + ' , ' + str(titre) + ' , ' + str(prixTtc) + ' , ' + str(prixHt) + ' , ' + str(numberAvail) + ' ,' + str(desc) + ' ,' + str(categ) + ' , ' + str(reviewR) + ' , ' + str(imageurl) + '\n' )

            #time.sleep(1) # pas nécessaire ici car le site est en libre accès (pour le moment!)


"""
