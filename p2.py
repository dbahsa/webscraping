"""

Résumé du projet de webscraping [4 étapes/demandes du client]:

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
        1b. sauvegarder le tout dans un fichier csv (à exclure de 'git'); je l'ai appelé ici 'oneProduct.csv'
    
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
        2b. Sauvegarder le tout dans un fichier csv (à exclure de 'git'); je l'ai appelé ici 'oneCategory.csv'

    3. Aller à la page d'acceuil:
        3a. Récupérer toutes les catégories
        3b. Récupérer les infos de chaque livre dans chaque catégorie comme ci-dessus (section '2')
        3c. Enregister le tout dans un fichier csv (à exclure de 'git'); je l'ai appelé ici 'allCategories.csv'
        3d. Télécharger dans un dossier 'images' les images de chaque livre dans chaque catégorie (à exclure de 'git')

    4. Sauvegarder ce script avec les fichiers requirements.txt et README.md sur GitHub, sans les dossiers 'env' et 'images', ni les fichiers csv d'ailleurs.

    NB:
        Mes Commits se font à l'issue de chacune de ces 4 étapes, dont le code de chaque étape sera ici mis sous forme 
        de commentaire sous de chaque partie suivante, pour pouvoir garder un visuel permamanet.  Ainsi à la fin de cet 
        exercice, la copie du code de la première étape sera tout en bas en dernier, précédée par celle de la deuxième et de la troisième étape.

"""

"""

Première étape:
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
        1b. sauvegarder le tout dans un fichier csv (à exclure de 'git'); je l'ai appelé ici 'oneProduct.csv'

"""

# Après avoir installer les paquest dans 'env', nous allons les importer pour rendre fonctionnel notre script
import requests # pip install requests
from bs4 import BeautifulSoup # pip install bs4 avec BeautifulSoup
import html.parser # pip install html-parser
# import time # timer entre pour chaque boucle
import soupsieve # pour pouvoir récupérer facilement du contenu html là où il n'y a pas de 'class' ni de 'id'



# l'url de la page produit pour effectuer notre 1er requête:
product_page_url = 'http://books.toscrape.com/catalogue/the-exiled_247/index.html'

# on va utiliser la méthode 'GET' pour charger l'url ci-dessus 
response = requests.get(product_page_url)


if response.status_code != 200:
    print("Le site est inaccessible.  Veuillez réessayer plus tard")
else:
    # print("Le site est accessible, vous pouvez continuer.")

    soup = BeautifulSoup(response.text, 'html.parser')

    print('URL de la page: ' + product_page_url) # pour imprimer l'url de la page produit
   
    links = [] # pour effectuer les boucles concernant les carateritiques des produits  
    tds = soup.find_all('td') 
    # print(len(tds)) == 7, ce qui nous permettra de créer un boucle pour le caractéristique des livres (upc, prix, etc.)
    # [print(td.text) for td in tds] : pour tester l'affichage du boucle avec les caractéristiques
    for td in tds:
        #a = td.find('a') # pour scraper les 'href'
        #link = a['href'] # pour scraper les 'href'
        #links.append('http://books.toscrape.com/' + link) pour scraper les 'href'
        links.append(td.text) # le lien pour scraper tous les 'td'
    print('universal_ product_code: {}'.format(links[0]))  # <=> print('UPC: ' + links[0])
    title = soup.find('h1') # trouver h1 pour lancer l'mpression du titre ci-dessous
    print('title: ' + title.text) # pour imprimer le titre du livre
    print('price_including_tax: {}'.format(links[2]).replace("Â", " ")) # pour imprimer le prix ttc du livre
    print('price_excluding_tax: {}'.format(links[3]).replace("Â", " "))  # pour imprimer le prix ht du livre
    print('number_available: {}'.format(links[5]).replace("In stock (", " ").replace(" available)", " ")) # pour imprimer la Q° dispo du livre - pas très beau, code à améliorer
    
    # Pour imrpimer la description de produit
    product_description = soup.select('.product_page > p')
    print('product_description: {}'.format(product_description).replace("<p>", " ").replace("</p>", " ").replace("[", " ").replace("]", " ") ) # l'affichage sort mais le contenu contient des crochets [] dans lequel le texte est entouré de tag <p></p>
    
    # Pour afficher la 'category'
    category = soup.find("ul", {"class":"breadcrumb"}).find_all('li')[2]
    catname = BeautifulSoup(str(category).replace("\n", " "), 'html.parser').get_text().encode("utf-8")
    print('category: ' + str(catname).replace("'", " ").replace('b', '')) # de la déco à enlever autour de la catégorie: 'b'\nMystery\n''
    
    # Pour afficher review_rating
    links = []
    review_rating = soup.find_all('p', {'class': 'star-rating'})
    for p in review_rating:  
        #print(image['src']) #print image source
        #print(image['alt']) #print alternate text
        link = p['class']
        links.append(link)
    print('review_rating: {}'.format(links[0]).replace("['star-rating',", " ").replace(']', '').replace("'", " ")) 

    # Pour afficher image_url
    links = []
    image_url = soup.find_all('img')
    for image in image_url:  
        #print(image['src']) #print image source
        #print(image['alt']) #print alternate text
        link = image['src']
        links.append('http://books.toscrape.com/' + link)
    print('image_url: {}'.format(links[0])) 
    # print(links[0]) # imprime sans l'en-tête



    """ 
    
    title = soup.find('title') 
    print(title.text) # pour imprimer le titre
    
    # ça imprime le contenu de la colonne 'upc'
    ths = soup.find_all('th')
    def my_ths(info):
        for y in info:
            print(y.text)          
    my_ths(ths)

    # ça imprime le contenu de la cellule à droite de 'upc', comme le fait '[print(td.text) for td in tds]'
    tds = soup.find_all('td')
    def my_tds(info):
        for x in info:
            print(x.text)          
    my_tds(tds)

    """
    