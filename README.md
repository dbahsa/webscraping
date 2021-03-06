# WEB SCRAPING
[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](#)[![forthebadge](https://forthebadge.com/images/badges/check-it-out.svg)](#)[![forthebadge](https://forthebadge.com/images/badges/made-with-markdown.svg)](#)

# POUR COMMENCER
_Nous allons expliquer ci-après comment créer et activer l'environnement virtuel Python, et aussi comment exécuter le code de l'application qui extrait les données du site books.toscrape.com_

### PRE-REQUIS

#### I. Création de l'environnement virtuel
1. Créer un répertoire **Projet** qui hébergera le projet en cours, puis vérifier à partir du terminal de votre ordinateur que vous y êtes placé, en exécutant ceci:
    >`$ mkdir Projet`(_pour créer le repertoire_)
`$ cd Projet` (_pour se placer dans le repertoire_)

2. Ajouter dans le repertoire **Projet** une copie du fichier **p2.py** (provenant du dossier compressé "P2_Nzimbi_Didier.zip").

3. Exécuter `$ python -m venv env` dans votre terminal pour créer l'environnement virtuel "**env**" pour faire fonctionner notre application avec les différents paquets requis (voir  fichier _requirements.txt_).  Vérifier tout de même que le répertoire **env** est bien crée en exécutant `$ ls` (**p2.py** et **env** devraient y figurer).  Maintenant, nous allons passer à l'étape d'activation.

#### II. Activation de l'environnement virtuel
1. Pour activer l'environnement virtuel à partir de votre terminal, veuillez exécuter la commande `source env/bin/activate`  (`env/Scripts/activate.bat` si vous êtes sous Windows). A ce stade, votre terminal doit ajoute le nom de votre environnement au début de chaque ligne de votre terminal (ici, **‘env’**).
2. Ensuite, pour que l'**environnement virtuel** soit **fonctionnel**, il va falloir **ajout**er les **paquets** Python requis à cet effet, soit en installant manuellement chaque paquet avec `pip`, soit en utilisant le fichier `requirements.txt` pour installer automatiquement tous les paquets.  Pour notre application, les paquets dont nous avons besoin sont `requests`, `bs4`,  `html.parser`,  `shutil`,    `csv23`,  `random`, et `soupsieve`,  qui peuvent être installés de la manière suivante.


### INSTALLATION

##### Installation _"manuelle"_
Avec `$ pip install` vous pouvez installer les paquets/modules requis pour le bon fonctionnement des sccripts. 

##### Installation _"automatique"_
Ajouter dans votre repertoire local **Projet** une copie du fichier _"requirements.txt"_ (provenant du dossier compressé "P2_Nzimbi_Didier.zip"), ensuite exécuter la commande:
> `$ pip install -r requirements.txt`

# DEMARRAGE
Voilà, vous pouvez dès à présent exécuter le script contenu dans le fichier `main.py`, en choisissant le type de contenu qui vous intéresse, ou bien vous pouvez également exécuter individuellement les fichiers ci-dessous :
1. `any_book.py`: Pour consulter les données d'un livre;
2. `books_any_category.py`: Pour voir les données de tous les livres d'une catégorie lambda;
3. `all_books_all_categories.py`: Pour obtenir les données de tous les livres de toutes les catégories;
4. `all_images.py`: Pour consulter toutes les images des livres du site.


# Fabriqué avec
* [DILLINGER](https://dillinger.io) - Editeur de texte
* [Forthebadge](http://forthebadge.com) - Badges en-tête
* Avec la contribution de Julien L. @ [Openclassrooms](http://Openclassrooms.com)

# Auteur
* **Didier K Nzimbi** _alias_ [dbahsa](https://github.com/dbahsa)