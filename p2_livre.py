# --- SOMMAIRE --- #

# 1. Demandes du client
# 2. Packages/Modules pré-requis
# 3. Script pour récupérer les données d'un livre pour les mettre dans un fichier csv
# 4. Conclusion

# ----- # ---- # ----- # ---- # ----- # ---- # ----- # ---- #


# 1. Demandes du client:

"""

Première étape: Scraping page produit - sans créer le fichier csv
    1. Choisir une page produit, 
        1a. Récupérer les infos suivantes:
            1a.1. product_page_url
            1a.2. universal_ product_code (upc)
            1a.3. title
            1a.4. price_including_tax
            1a.5. price_excluding_tax
            1a.6. number_available
            1a.7. product_description
            1a.8. category
            1a.9. review_rating
            1a.10. image_url
        1b. sauvegarder le tout dans un fichier csv (à exclure de 'git'); je l'ai appelé ici 'p2_livre.csv'

"""

# ----- # ---- # ----- # ---- # ----- # ---- # ----- # ---- #


# 2. Packages/Modules pré-requis

import requests # pour envoyer des requêtes HTTP via Python
from bs4 import BeautifulSoup # pour faciliter l'extraction des liens de notre page web
import html.parser # pour parser le contenu html
import soupsieve # pour récupérer facilement du contenu html là où il n'y a pas de 'class' ni de 'id'
import time # pour mettre un delai en sec entre chaque boucle pour éviter la procédure d'être bloqué par le serveur du site d'extraction


# ----- # ---- # ----- # ---- # ----- # ---- # ----- # ---- #


# 3. Script pour récupérer les données d'un livre pour les mettre dans un fichier csv



#""" 

with open('p2_livre.csv', 'w') as outf: # on crée notre fichier csv après avoir traversé toutes les pages contenues dans 'booksUrls.txt' 
        # outf.write(): pour créer l'en-tête de 'p2_categorie.csv'
    outf.write('product_page_url, universal_product_code, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url\n')
        #for row in inf: # nous utilisons le fichier 'booksUrls.txt'  pour scraper les données de chaque livre de la catégorie 'mystery'
    product_page_url = 'http://books.toscrape.com/catalogue/the-exiled_247/index.html'

            # on va utiliser la méthode 'GET' pour charger l'url chaque page des livres de la catégorie 'mystery' via 'product_page_url' contenu dans 'booksUrls.txt'
    response = requests.get(product_page_url)

    if response.status_code != 200:
        print("Le site est inaccessible.  Veuillez réessayer plus tard")
    else:
        # print("Le site est accessible, vous pouvez continuer.") # pas vraiment nécessaire ici vu que le script fonctionne

        soup = BeautifulSoup(response.text, 'html.parser')

                # --- les lignes ci-après concernent l'extraction des données de chaque livre --- #

                # pour afficher l'url de la page produit en cours de traitement
        prodUrl = product_page_url
        print(prodUrl)
                
                # pour effectuer les boucles concernant les carateritiques des produits 
        links = []  
        tds = soup.find_all('td') 
                # print(len(tds)) == 7, ce qui nous permettra de créer un boucle pour le caractéristique des livres (upc, prix, etc.)
                # pour tester l'affichage du boucle avec les caractéristiques: [print(td.text) for td in tds]
        for td in tds:
                    #a = td.find('a') # pour scraper les 'href'
                    #link = a['href'] # pour scraper les 'href'
                    #links.append('http://books.toscrape.com/' + link) pour scraper les 'href'
            links.append(td.text) # le lien pour scraper tous les 'td'
                
                # pour afficher l'UPC de chaque livre
        upc = links[0]
        print(upc) # une autre façon de l'écrire: print('universal_product_code: {}'.format(links[0]))  # <=> print(f'"UPC: " + links[0]')

                # pour afficher le titre de chaque livre  
        title = soup.find('h1') # trouver h1 pour lancer afficher le titre
        titre = title.text.replace(",", " -")
        print(titre)

                # pour afficher le prix ttc du livre # print('price_including_tax: {}'.format(links[2]).replace("Â", " ")): on est parti de ce code pour écrire ce qui suit:
        prixTtc = links[2].replace("Â", " ")
        print(prixTtc)

                # pour afficher le prix ht du livre # print('price_excluding_tax: {}'.format(links[3]).replace("Â", " ")) 
        prixHt = links[3].replace("Â", " ")
        print(prixHt)

                # pour obtenir la quantité dispo du livre => pas très beau, code à améliorer, un peu comme partout :) #print('number_available: {}'.format(links[5]).replace("In stock (", " ").replace(" available)", " ")) 
        numberAvail = links[5].replace("In stock (", " ").replace(" available)", " ")
        print(numberAvail)

                # Pour extraire la description de produit
        product_description = soup.select('.product_page > p')
        desc = str(product_description).replace(",", "_").replace('<p>', ' ').replace('</p>', ' ').replace('[', ' ').replace(']', ' ')
        print(desc) # l'affichage sort mais le contenu contient des crochets [] dans lequel le texte est entouré de tag <p></p>
                # ci-dessus, la virgule dans tout le contenu a été remplacée par '_' pour être capable de conserver cette donnée dans la colonne 'product_description'

                # Pour afficher la 'category'
        category = soup.find("ul", {"class":"breadcrumb"}).find_all('li')[2]
        catname = BeautifulSoup(str(category).replace("\n", " "), 'html.parser').get_text().encode("utf-8")
        categ = str(catname).replace("'", " ").replace('b', '')
        print(categ) # de la déco à enlever autour de la catégorie: 'b'\nMystery\n''

                # Pour afficher review_rating
        links = []
        review_rating = soup.find_all('p', {'class': 'star-rating'})
        for p in review_rating:
            link = p['class'][1]
            links.append(link)
        reviewR = links[0].replace("['star-rating',", " ").replace("]", "").replace("'", " ")
        print(reviewR) # le code suivant a été utilisé pour obtenir ce qui précède pour obtenir 'reviewR': print(f'review_rating: {link[0].replace("[", "").replace("'", "").replace("star-rating',", "").replace("]", "").replace("'", "")}') # f-string ne fonctionne pas non plus ici

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

#"""

# ----- # ---- # ----- # ---- # ----- # ---- # ----- # ---- #


# 5. Conclusion
    
"""
    La première étape est terminée. Nous avons pu extraire et sauvegarder les données d'un livre dans le fichier 'p2_livre.csv'.
    Vous pouvez dès à présent consulter le fichier 'p2_categorie.py', qui permet d'extraire les données de tous les ouvrages d'une catégorie précise.
    Merci :)
"""