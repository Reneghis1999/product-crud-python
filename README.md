# Product CRUD Python

## Description
Ce projet est un exemple de gestion de produits en **Python** utilisant la **programmation orientée objet (POO)**.  
Il permet de créer, lire, mettre à jour et supprimer des produits via un **menu en ligne de commande (CLI)**.

Le projet est conçu pour être **simple, lisible et facilement extensible**, parfait 
pour comprendre la POO 
---

## Fonctionnalités

- Ajouter un produit avec ID, nom, prix et quantité
- Chercher un produit par ID
- Mettre à jour un produit (nom, prix, quantité)
- Supprimer un produit
- Lister tous les produits

---

## Structure du projet

product-crud-python/ (nom du repository)

main.py # Point d'entrée du programme 
product.py # Classe Product (entité produit)
product_manager.py # Classe ProductManager (le CRUD)
README.md # Ce fichier
gitignore # Pour ignorer les fichiers inutiles (venv, pycache, etc.)



---

## Installation et exécution

1. Cloner le dépôt :  
```bash
git clone <URL_DU_DEPOT>
cd product-crud-python



Créer un environnement virtuel :

python -m venv venv
source venv/bin/activate   # Sur Linux/Mac
venv\Scripts\activate      # Sur Windows


Lancer le programme :
python main.py


Suivre le menu pour ajouter, chercher, modifier, supprimer ou lister des produits.

exemple d'utilisation

=== Gestion des Produits ===
1. Ajouter un produit
2. Chercher un produit par ID
3. Mettre à jour un produit
4. Supprimer un produit
5. Lister tous les produits
6. Quitter
Choisis une option (1-6) : 1
ID du produit : 1
Nom : Stylo
Prix : 2.5
Quantité : 10
Produit ajouté : Stylo (ID 1)

Commandes Git utilisées pour chaque étape :

git add <fichier>
git commit -m "001-initialize-project-structure" (structure et fichiers du projet)
git commit -m "002-implement-product-entity" (classe produit)
git commit -m "003-add-ProductManager-class-with-CRUD"(classe product manager avec CRUD)
git commit -m "004-add-main-cli-to-test-ProductManager" (creation de main avec un menu)
git push


Auteur

NAYO René-Ghislain – Stagiaire developpement backend Python / Développement POO
