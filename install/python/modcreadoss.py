#!/usr/bin/python3.9
# -*-coding:Latin-1 -*

"""Ce module permet la création à l'emplacement où il se situe, d'un dossier STOCKAGE, avec deux sous-dossiers PROFS et ELEVES.
Dans ces deux sous dossiers, chaque élève ou professeur a son dossier personnel à son nom d'utilisateur de l'Active Directory Windows
Version 1.0 - Le 16/01/2021 - Par Michaël Durand - étudiant AIC OPENCLASSROOM"""

# Importation des modules
import os
import pyad.adquery


# Creation du dossier de STOCKAGE pour les documents des ELEVES et des PROFS
if not os.path.exists("STOCKAGE"):
        os.mkdir ("STOCKAGE")

# Creation du sous-dossier PROFS
path = os.path.join('STOCKAGE', 'PROFS')
if not os.path.exists(path):
        os.mkdir (path)

# Creation du sous-dossier ELEVES
path = os.path.join('STOCKAGE', 'ELEVES')
if not os.path.exists(path):
        os.mkdir (path)


# Appel de la fonction ADQuery pour rechercher les utilisateurs
q = pyad.adquery.ADQuery()


# Recherche dans l'Active Directory des utilisateurs de l'unité organisationnelle PROFS
q.execute_query(
attributes = ["CN"],
where_clause = "objectClass = 'USER'",
base_dn = "OU=PROFS, DC=ad, DC=salleinfo1, DC=com"
)

# Pour chaque utilisateur trouvé dans l'unité organisationnelle PROFS,
# création d'un dossier à son nom dans le dossier de STOCKAGE, sous-dossier PROFS 
for row in q.get_results():
        path = os.path.join('STOCKAGE', 'PROFS', row ["CN"])
        if not os.path.exists(path):
                os.mkdir (path)


# Recherche dans l'Active Directory des utilisateurs de l'unité organisationnelle ELEVES
q.execute_query(
attributes = ["CN"],
where_clause = "objectClass = 'USER'",
base_dn = "OU=ELEVES, DC=ad, DC=salleinfo1, DC=com"
)

# Pour chaque utilisateur trouvé dans l'unité organisationnelle ELEVES,
# création d'un dossier à son nom dans le dossier de STOCKAGE, sous-dossier ELEVES 
for row in q.get_results():
        path = os.path.join('STOCKAGE', 'ELEVES', row ["CN"])
        if not os.path.exists(path):
                os.mkdir (path)
