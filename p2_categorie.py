# --- SOMMAIRE --- #

# 1. Demandes du client
# 2. Packages/Modules pré-requis
# 3. Script pour récupérer les urls des livres d'une catégorie pour les mettre dans un fichier csv
# 4. Script pour extraire et sauvegarde en csv toutes les données des ouvrages d'une catégorie
# 5. Conclusion

# ----- # ---- # ----- # ---- # ----- # ---- # ----- # ---- #


# 1. Demandes du client:

"""

Deuxième étape: Appliquer "Etape 1" aux produits d'une catégorie
    2. Choisir une catégorie, puis récupérer les infos suivantes:
        2a. Récupérer pour chaque livre les infos suivantes:
            2a.1. product_page_url
            2a.2. universal_ product_code (upc)
            2a.3. title
            2a.4. price_including_tax
            2a.5. price_excluding_tax
            2a.6. number_available
            2a.7. product_description
            2a.8. category
            2a.9. review_rating
            2a.10. image_url
        2b. Sauvegarder le tout dans un fichier csv (à exclure de 'git'); je l'ai appelé ici 'p2_categorie.csv'

"""

# ----- # ---- # ----- # ---- # ----- # ---- # ----- # ---- #


# 2. Packages/Modules pré-requis

import requests # pour envoyer des requêtes HTTP via Python
from bs4 import BeautifulSoup # pour faciliter l'extraction des liens de notre page web
import html.parser # pour parser le contenu html
import soupsieve # pour récupérer facilement du contenu html là où il n'y a pas de 'class' ni de 'id'
import time # pour mettre un delai en sec entre chaque boucle pour éviter la procédure d'être bloqué par le serveur du site d'extraction


# ----- # ---- # ----- # ---- # ----- # ---- # ----- # ---- #


# 3. Script pour récupérer les urls des livres d'une catégorie pour les mettre dans un fichier csv

"""

Info catégorie: 
    - Mystery;
    - 32 livres sur 2 pages;
    - url: http://books.toscrape.com/catalogue/category/books/mystery_3/page-1.html

"""


# Script pour extraire les données des 2 pages de la catégorie 'Mystery':


"""

links = []

for i in range(1, 3):
    url = 'http://books.toscrape.com/catalogue/category/books/mystery_3/page-' + str(i) + '.html'
    response = requests.get(url)

    if response.status_code != 200:
        print("Le site est inaccessible.  Veuillez réessayer plus tard")
    else:
        soup = BeautifulSoup(response.text, 'html.parser')
        print('Page: ' + str(i))

        # Pour afficher l'url de chaque livre dans une catégorie
        book_urls = soup.find_all("article", {"class":"product_pod"})
        for book_url in book_urls:  
            a = book_url.find('a')
            link = a['href'].replace('../../../', '')
            links.append('http://books.toscrape.com/catalogue/' + link)
        time.sleep(1) # pour ralentir le boucle de 1sec pour éventuellement éviter que l'extraction des données soit bloquée

print(len(links))

with open('booksUrls.txt', 'w') as file: # booksUrls.txt contient les urls de chaque livre de la catégorie "mystery"
    for link in links: # nous allons utiliser booksUrls.txt pour scraper les données de chaque livre de la catégorie 'mystery'
        file.write(link + '\n')

"""


# ----- # ---- # ----- # ---- # ----- # ---- # ----- # ---- #


# 4. Script pour extraire et sauvegarder en csv toutes les données des ouvrages d'une catégorie

#""" 

with open('booksUrls.txt', 'r') as inf: # 'booksUrls.txt' contient les urls de chaque livre de la catégorie "mystery"
    with open('p2_categorie.csv', 'w') as outf: # on crée notre fichier csv après avoir traversé toutes les pages contenues dans 'booksUrls.txt' 
        # outf.write(): pour créer l'en-tête de 'p2_categorie.csv'
        outf.write('product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url\n')
        for row in inf: # nous utilisons le fichier 'booksUrls.txt'  pour scraper les données de chaque livre de la catégorie 'mystery'
            product_page_url = row.strip()

            response = requests.get(product_page_url)

            if response.status_code != 200:
                print("Le site est inaccessible.  Veuillez réessayer plus tard")
            else:
                
                soup = BeautifulSoup(response.text, 'html.parser')

                # --- les lignes ci-après concernent l'extraction des données de chaque livre --- #

                # pour afficher l'url de la page produit en cours de traitement
                prodUrl = product_page_url
                print(prodUrl)
                
                # pour obtenir les carateritiques de chaque livre 
                links = []  
                tds = soup.find_all('td') 
                
                # pour tester l'affichage les caractéristiques de chaque livre 
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

                # Pour extraire la description de chaque livre 
                product_description = soup.select('.product_page > p')
                desc = str(product_description).replace('<p>', ' ').replace('</p>', ' ').replace('[', '"').replace(']', '"')
                print(desc)

                # Pour afficher la categorie de chaque livre
                category = soup.find("ul", {"class":"breadcrumb"}).find_all('li')[2]
                catname = BeautifulSoup(str(category).replace("\n", " "), 'html.parser').get_text().encode("utf-8")
                categ = str(catname).replace("'", " ").replace('b', '')
                print(categ) 

                # Pour afficher le review_rating de chaque livre 
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
                print(imageurl)

                outf.write(str(prodUrl) + ' , ' + str(upc) + ' , ' + str(titre) + ' , ' + str(prixTtc) + ' , ' + str(prixHt) + ' , ' + str(numberAvail) + ' ,' + str(desc) + ' ,' + str(categ) + ' , ' + str(reviewR) + ' , ' + str(imageurl) + '\n' )


#"""

# ----- # ---- # ----- # ---- # ----- # ---- # ----- # ---- #


# 5. Conclusion
    
"""
    C'est fini pour cette section dans laquelle nous avons pu traverser une page catégorie afin d'extraire le contenu de tous ses livres, accessible sur 'p2_categorie.csv'.
    Vous pouvez dès à présent consulter le fichier 'p2_site.py', qui permet d'extraire les données de tous les ouvrages vendus sur 'books.toscrape.com'.
    Merci :)
"""