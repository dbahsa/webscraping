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
import shutil

# ----- # ---- # ----- # ---- # ----- # ---- # ----- # ---- #


# 3a. Script pour Extraire toutes les catégories de livres disponibles:

"""

Info catégories: 
    - Quantité: 50
    - Scrapées à partir: http://books.toscrape.com/
    - Le fichier contenant les urls des catégories: categsUrls.txt

"""


# ----- # ---- # ----- # ---- # ----- # ---- # ----- # ---- #


# 3b. Script pour extraire les informations produit de tous les livres appartenant à toutes les différentes catégories:
    # 3b.1. Extractiion et sauvegarde dans 'allBooksUrls.txt' de tous les urls de tous les livres à partir de la page d'accueil;
    # 3b.2. Sauvegarde dans 'allBooksUrls.csv' des données de tous les livres du site
    



# -- Script pour créer le fichier contenant l'image de chaque page Produit consultée

"""

links = []

for i in range(1, 51):
    url = 'http://books.toscrape.com/catalogue/page-' + str(i) + '.html'
    response = requests.get(url)

    if response.status_code != 200:
        print("Le site est inaccessible.  Veuillez réessayer plus tard")
    else:
        soup = BeautifulSoup(response.text, 'html.parser')
        #print('Page: ' + str(i))
        
        # Pour afficher image_url
        image_url = soup.find_all('img')
        for image in image_url:  
            link = image['src']
            links.append('http://books.toscrape.com/' + link)
    
        #time.sleep(1) # pour ralentir le boucle de 1sec pour éventuellement éviter que l'extraction des données soit bloquée

#print(links)

with open('imageUrls.txt', 'w') as file: 
    for link in links: 
        file.write(link + '\n')

"""


# -- Script pour télécharger et enregistrer le fichier image de chaque page Produit consultée

#""" 

with open('imageUrls.txt', 'r') as inf:
    for row in inf: 
        image_url = row.strip()

        imageName = image_url.split('/')[-1]

        response = requests.get(image_url,stream=True)

        if response.status_code != 200:
            print("Le site est inaccessible.  Veuillez réessayer plus tard")
        else:
                
            response.raw.decode_content = True
            with open(imageName, 'wb') as f:
                shutil.copyfileobj(response.raw,f)


#"""

""" pour sraper une seule image

image_url = 'http://books.toscrape.com/../media/cache/d7/0f/d70f7edd92705c45a82118c3ff6c299d.jpg'

imageName = image_url.split('/')[-1]

response = requests.get(image_url,stream=True)

if response.status_code != 200:
    print("Le site est inaccessible.  Veuillez réessayer plus tard")
else:
                
    response.raw.decode_content = True

    with open(imageName, 'wb') as f:
        shutil.copyfileobj(response.raw,f)

"""
