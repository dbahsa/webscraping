# --- SOMMAIRE --- #

"""

Résumé du projet de webscraping, en 4 étapes (demandes-client):

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

# --- SCRIPTS --- #

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
        2b. Sauvegarder le tout dans un fichier csv (à exclure de 'git'); je l'ai appelé ici 'oneCategory.csv'


"""

# Après avoir installer les paquest dans 'env', nous allons les importer pour rendre fonctionnel notre script
import requests # pip install requests
from bs4 import BeautifulSoup # pip install bs4 avec BeautifulSoup
import html.parser # pip install html-parser
import time # timer entre chaque boucle pour éviter la procédure d'être bloqué par le serveur du site d'extraction
import soupsieve # pour pouvoir récupérer facilement du contenu html là où il n'y a pas de 'class' ni de 'id'


# utliser fct° 
# def getBookInfo(product_page_url = 'http://books.toscrape.com/catalogue/the-exiled_247/index.html')
# getBookInfo used for e.a. categ & items... check out python.org on fct° for scraping

"""

with open('urls.txt', 'r') as inf: 
    # l'avantage de lire un fichier de cette façon (dynamique), 
    # est que le fichier se ferme automatiquement après sa lecture (quand on sort de l'indentation),
    # autrement on peut l'écrire également tel que:
    # file = open('urls.txt', 'r') 

    with open('oneProduct.csv', 'w') as outf:

        outf.write('product_page_url, universal_ product_code, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url\n')

        for row in inf:
            print(row) # pour afficher chaque url avec un saut de ligne
            product_page_url = row.strip() #url = row.strip() #product_page_url = 'http://books.toscrape.com/catalogue/the-exiled_247/index.html' # l'url de la page produit pour effectuer notre 1er requête
            response = requests.get(product_page_url) #response = requests.get(url) #response = requests.get(product_page_url) # on va utiliser la méthode 'GET' pour charger l'url ci-dessus 
            print(response.encoding)

"""


#"""
# --- Script pour extraire les données des 2 pages de la catégorie 'Mystery' --- #

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
        time.sleep(1) # pour ralentir le boucle de 2sec pour éviter que l'extraction d'être bloquée

print(len(links))

with open('booksUrls.txt', 'w') as file: # ce fichier 'booksUrls.txt' contient les urls de chaque livre de la catégorie "mysterie"
    for link in links: # nous allons éventuellement l'utiliser pour scraper les données de chaque livre de la catégorie 'mystery'
        file.write(link + '\n')


# --- # --- #

#"""


# --- Script pour afficher les url de chaque livre d'une catégorie bien précise --- #

""" 

# l'url de la page produit pour effectuer notre 1er requête:
url = 'http://books.toscrape.com/catalogue/category/books/mystery_3/page-2.html'

# on va utiliser la méthode 'GET' pour charger l'url ci-dessus 
response = requests.get(url)

if response.status_code != 200:
    print("Le site est inaccessible.  Veuillez réessayer plus tard")
else:
    # print("Le site est accessible, vous pouvez continuer.")

    
    soup = BeautifulSoup(response.text, 'html.parser')

    # on va récupérer les liens de chaque livre d'une catégorie bien précise
    # li.col-xs-6:nth-child(1) > article:nth-child(1) > h3:nth-child(3) > a:nth-child(1)

    links = []
    book_urls = soup.find_all("article", {"class":"product_pod"})
    for book_url in book_urls:  
        #print(image['src']) #print image source
        #print(image['alt']) #print alternate text
        a = book_url.find('a')
        link = a['href'].replace('../../../', '')
        links.append('http://books.toscrape.com/catalogue/' + link)
    print(links)
    #print('image_url: {}'.format(links[0])) 

    # les pages de la catégorie "mystery": 
        # http://books.toscrape.com/catalogue/category/books/mystery_3/page-1.html 
        # http://books.toscrape.com/catalogue/category/books/mystery_3/page-2.html
    
"""
    
""" books' container
    
    <article class="product_pod">
            <div class="image_container">
                <a href="../../../sharp-objects_997/index.html">
                    <img src="../../../../media/cache/32/51/3251cf3a3412f53f339e42cac2134093.jpg" alt="Sharp Objects" class="thumbnail">
                </a>
            </div>
            <p class="star-rating Four">
            <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
            </p>
            <h3>
                <a href="../../../sharp-objects_997/index.html" title="Sharp Objects">Sharp Objects</a>
            </h3>
            <div class="product_price">
                <p class="price_color">£47.82</p>
                <p class="instock availability">
                    <i class="icon-ok"></i>In stock
                </p>
                <form>
                    <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
                </form>
            </div>
        </article>
    
"""

# ----- # ---- #


# --- Etape intermediaire btw bookpage & categ page -- Script pour afficher les info d'un livre bien précis sur une page donnée --- #


""" 


# l'url de la page produit pour effectuer notre 1er requête:
product_page_url = 'http://books.toscrape.com/catalogue/the-exiled_247/index.html'

# on va utiliser la méthode 'GET' pour charger l'url ci-dessus 
response = requests.get(product_page_url)

if response.status_code != 200:
    print("Le site est inaccessible.  Veuillez réessayer plus tard")
else:
            # print("Le site est accessible, vous pouvez continuer.")

    soup = BeautifulSoup(response.text, 'html.parser')

    #print('URL de la page: ' + product_page_url) # pour imprimer l'url de la page produit
    print(f'product_page_url: {product_page_url}')
        
    links = [] # pour effectuer les boucles concernant les carateritiques des produits  
    tds = soup.find_all('td') 
    # print(len(tds)) == 7, ce qui nous permettra de créer un boucle pour le caractéristique des livres (upc, prix, etc.)
    # [print(td.text) for td in tds] : pour tester l'affichage du boucle avec les caractéristiques
    for td in tds:
        #a = td.find('a') # pour scraper les 'href'
        #link = a['href'] # pour scraper les 'href'
        #links.append('http://books.toscrape.com/' + link) pour scraper les 'href'
        links.append(td.text) # le lien pour scraper tous les 'td'
    #print('universal_product_code: {}'.format(links[0]))  # <=> print('UPC: ' + links[0])
    print(f'universal_product_code: {links[0]}')
            
    title = soup.find('h1') # trouver h1 pour lancer l'mpression du titre ci-dessous
    #print('title: ' + title.text) # pour imprimer le titre du livre
    print(f'title: {title.text}')

    #print('price_including_tax: {}'.format(links[2]).replace("Â", " ")) # pour imprimer le prix ttc du livre
    print(f'price_including_tax: {links[2].replace("Â", " ")}')

    #print('price_excluding_tax: {}'.format(links[3]).replace("Â", " "))  # pour imprimer le prix ht du livre
    print(f'price_excluding_tax: {links[3].replace("Â", " ")}')

    #print('number_available: {}'.format(links[5]).replace("In stock (", " ").replace(" available)", " ")) # pour imprimer la Q° dispo du livre - pas très beau, code à améliorer
    print(f'number_available: {links[5].replace("In stock (", " ").replace(" available)", " ")}')

    # Pour imrpimer la description de produit
    product_description = soup.select('.product_page > p')
    print('product_description: {}'.format(product_description).replace("<p>", " ").replace("</p>", " ").replace("[", " ").replace("]", " ")) # l'affichage sort mais le contenu contient des crochets [] dans lequel le texte est entouré de tag <p></p>
    # print(f'product_description: {product_description.replace("<p>", " ").replace("</p>", " ").replace("[", " ").replace("]", " ")}') # f-string ici ne fonctionne pas

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
        link = p['class'][1]
        links.append(link)
    print('review_rating: {}'.format(links[0]).replace("['star-rating',", " ").replace("]", "").replace("'", " ")) 
    # print(f'review_rating: {link[0].replace("[", "").replace("'", "").replace("star-rating',", "").replace("]", "").replace("'", "")}') # f-string ne fonctionne pas non plus ici

    # Pour afficher image_url
    links = []
    image_url = soup.find_all('img')
    for image in image_url:  
        #print(image['src']) #print image source
        #print(image['alt']) #print alternate text
        link = image['src']
        links.append('http://books.toscrape.com/' + link)
    imageurl = 'image_url: {}'.format(links[0])
    print(imageurl) 
    # print(links[0]) # imprime sans l'en-tête

    # Pour sauvegarder dans un fichier externe
    #f = open('oneProduct.txt', 'r')
    #f.write(f'product_page_url: {product_page_url}' + ' , ' + f'universal_product_code: {links[0]}' + ' , ' + f'title: {title.text}' + ' , ' + f'price_including_tax: {links[2].replace("Â", " ")}' + ' , ' + f'price_excluding_tax: {links[3].replace("Â", " ")}' + ' , ' + f'number_available: {links[5].replace("In stock (", " ").replace(" available)", " ")}' + ' , ' + 'product_description: {}'.format(product_description).replace("<p>", " ").replace("</p>", " ").replace("[", " ").replace("]", " ") + ' , ' + 'category: ' + str(catname).replace("'", " ").replace('b', '') + ' , ' + 'review_rating: {}'.format(links[0]).replace("['star-rating',", " ").replace("]", "").replace("'", " ") + ' , ' + 'image_url: {}'.format(links[0]) + '\n' )
    #for row in f:
    #    print(row)
    #f.close()

"""

 # --- # --- #


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
        1b. sauvegarder le tout dans un fichier csv (à exclure de 'git'); je l'ai appelé ici 'oneProduct.csv'

        
        # Après avoir installer les paquest dans 'env', nous allons les importer pour rendre fonctionnel notre script
        import requests # pip install requests
        from bs4 import BeautifulSoup # pip install bs4 avec BeautifulSoup
        import html.parser # pip install html-parser
        # import time # timer entre pour chaque boucle
        import soupsieve # pour pouvoir récupérer facilement du contenu html là où il n'y a pas de 'class' ni de 'id'


        # utliser fct° 
        # def getBookInfo(product_page_url = 'http://books.toscrape.com/catalogue/the-exiled_247/index.html')
        # getBookInfo used for e.a. categ & items... check out python.org on fct° for scraping

        # l'url de la page produit pour effectuer notre 1er requête:
        product_page_url = 'http://books.toscrape.com/catalogue/the-exiled_247/index.html'

        # on va utiliser la méthode 'GET' pour charger l'url ci-dessus 
        response = requests.get(product_page_url)


        if response.status_code != 200:
            print("Le site est inaccessible.  Veuillez réessayer plus tard")
        else:
            # print("Le site est accessible, vous pouvez continuer.")

            soup = BeautifulSoup(response.text, 'html.parser')

            #print('URL de la page: ' + product_page_url) # pour imprimer l'url de la page produit
            print(f'product_page_url: {product_page_url}')
        
            links = [] # pour effectuer les boucles concernant les carateritiques des produits  
            tds = soup.find_all('td') 
            # print(len(tds)) == 7, ce qui nous permettra de créer un boucle pour le caractéristique des livres (upc, prix, etc.)
            # [print(td.text) for td in tds] : pour tester l'affichage du boucle avec les caractéristiques
            for td in tds:
                #a = td.find('a') # pour scraper les 'href'
                #link = a['href'] # pour scraper les 'href'
                #links.append('http://books.toscrape.com/' + link) pour scraper les 'href'
                links.append(td.text) # le lien pour scraper tous les 'td'
            #print('universal_product_code: {}'.format(links[0]))  # <=> print('UPC: ' + links[0])
            print(f'universal_product_code: {links[0]}')
            
            title = soup.find('h1') # trouver h1 pour lancer l'mpression du titre ci-dessous
            #print('title: ' + title.text) # pour imprimer le titre du livre
            print(f'title: {title.text}')

            #print('price_including_tax: {}'.format(links[2]).replace("Â", " ")) # pour imprimer le prix ttc du livre
            print(f'price_including_tax: {links[2].replace("Â", " ")}')

            #print('price_excluding_tax: {}'.format(links[3]).replace("Â", " "))  # pour imprimer le prix ht du livre
            print(f'price_excluding_tax: {links[3].replace("Â", " ")}')

            #print('number_available: {}'.format(links[5]).replace("In stock (", " ").replace(" available)", " ")) # pour imprimer la Q° dispo du livre - pas très beau, code à améliorer
            print(f'number_available: {links[5].replace("In stock (", " ").replace(" available)", " ")}')

            # Pour imrpimer la description de produit
            product_description = soup.select('.product_page > p')
            print('product_description: {}'.format(product_description).replace("<p>", " ").replace("</p>", " ").replace("[", " ").replace("]", " ") ) # l'affichage sort mais le contenu contient des crochets [] dans lequel le texte est entouré de tag <p></p>
            # print(f'product_description: {product_description.replace("<p>", " ").replace("</p>", " ").replace("[", " ").replace("]", " ")}') # f-string ici ne fonctionne pas

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
                link = p['class'][1]
                links.append(link)
            print('review_rating: {}'.format(links[0]).replace("['star-rating',", " ").replace("]", "").replace("'", " ")) 
            # print(f'review_rating: {link[0].replace("[", "").replace("'", "").replace("star-rating',", "").replace("]", "").replace("'", "")}') # f-string ne fonctionne pas non plus ici

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

# -- 1 -- Script pour extraire les infos d'une page produit sans le mettre dans un fichier csv --- #

"""

# l'url de la page produit pour effectuer notre 1er requête:
product_page_url = 'http://books.toscrape.com/catalogue/the-exiled_247/index.html'

# on va utiliser la méthode 'GET' pour charger l'url ci-dessus 
response = requests.get(product_page_url)

if response.status_code != 200:
    print("Le site est inaccessible.  Veuillez réessayer plus tard")
else:
            # print("Le site est accessible, vous pouvez continuer.")

    soup = BeautifulSoup(response.text, 'html.parser')

    #print('URL de la page: ' + product_page_url) # pour imprimer l'url de la page produit
    print(f'product_page_url: {product_page_url}')
        
    links = [] # pour effectuer les boucles concernant les carateritiques des produits  
    tds = soup.find_all('td') 
    # print(len(tds)) == 7, ce qui nous permettra de créer un boucle pour le caractéristique des livres (upc, prix, etc.)
    # [print(td.text) for td in tds] : pour tester l'affichage du boucle avec les caractéristiques
    for td in tds:
        #a = td.find('a') # pour scraper les 'href'
        #link = a['href'] # pour scraper les 'href'
        #links.append('http://books.toscrape.com/' + link) pour scraper les 'href'
        links.append(td.text) # le lien pour scraper tous les 'td'
    #print('universal_product_code: {}'.format(links[0]))  # <=> print('UPC: ' + links[0])
    print(f'universal_product_code: {links[0]}')
            
    title = soup.find('h1') # trouver h1 pour lancer l'mpression du titre ci-dessous
    #print('title: ' + title.text) # pour imprimer le titre du livre
    print(f'title: {title.text}')

    #print('price_including_tax: {}'.format(links[2]).replace("Â", " ")) # pour imprimer le prix ttc du livre
    print(f'price_including_tax: {links[2].replace("Â", " ")}')

    #print('price_excluding_tax: {}'.format(links[3]).replace("Â", " "))  # pour imprimer le prix ht du livre
    print(f'price_excluding_tax: {links[3].replace("Â", " ")}')

    #print('number_available: {}'.format(links[5]).replace("In stock (", " ").replace(" available)", " ")) # pour imprimer la Q° dispo du livre - pas très beau, code à améliorer
    print(f'number_available: {links[5].replace("In stock (", " ").replace(" available)", " ")}')

    # Pour imrpimer la description de produit
    product_description = soup.select('.product_page > p')
    print('product_description: {}'.format(product_description).replace("<p>", " ").replace("</p>", " ").replace("[", " ").replace("]", " ") ) # l'affichage sort mais le contenu contient des crochets [] dans lequel le texte est entouré de tag <p></p>
    # print(f'product_description: {product_description.replace("<p>", " ").replace("</p>", " ").replace("[", " ").replace("]", " ")}') # f-string ici ne fonctionne pas

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
        link = p['class'][1]
        links.append(link)
    print('review_rating: {}'.format(links[0]).replace("['star-rating',", " ").replace("]", "").replace("'", " ")) 
    # print(f'review_rating: {link[0].replace("[", "").replace("'", "").replace("star-rating',", "").replace("]", "").replace("'", "")}') # f-string ne fonctionne pas non plus ici

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