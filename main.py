# --- SOMMAIRE --- # 
# 1. Extraction et sauvegarde sous csv les données d'un livre
# 2. Extraction et sauvegarde sous csv les données de tous les livres d'une catégorie
# 3. Extraction et sauvegarde dans différents fichiers csv de données de tous les livres de toutes les catégories
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
import os, sys # pour créer un dossier

# -- Import de fichier individuel pour le traitement sur le fichier principal -- #
import all_books_all_categories
import books_any_category
import any_book
import all_images



# ----- # ---- # ----- # ---- # ----- # ---- # ----- # ---- #
# -- Fichier principal pour exécuter tous les scripts à la demande  -- #

if __name__=="__main__":
        
        message = "Choisissez votre script:\n Taper '1' pour extraire les données d'un livre d'une catégéorie quelconque;\n Taper '2' pour extraire les données de tous les livres d'une catégorie;\n Taper '3' pour scraper les données de tous les livres vendus sur le site;\n Taper '4' pour récupérer toutes les images page_produit du site."
        print(message)

        x = int(input("Taper votre choix: "))

        
        def all_scripts(user_choice):
                
                if user_choice == 1:
                        print('Le script est lancé... Veuillez patienter un petit instant svp.')
                        any_book.book_function2()
                        
                elif user_choice == 2:
                        print('Le script est lancé... Veuillez patienter un petit moment svp.')
                        books_any_category.books_function2()
                        
                elif user_choice == 3:
                        print('Le script est lancé... Veuillez patienter un petit moment svp.')
                        all_books_all_categories.all_books_function2()
                
                elif user_choice == 4:
                        print('Le script est lancé... Cela va prendre quelques minutes. Merci de votre patience.')
                        all_images.image_function2()
                
                elif user_choice < 1 or user_choice > 4 :
                        print('Votre choix est hors porté. Merci de relancer le script svp.')
        
        all_scripts(x)
