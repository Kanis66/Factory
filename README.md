# Factory-WP (Version 01)

## Mise en place d'un Wordpress sur un serveur Windows.



### Descriptif :

Ce projet vise à automatiser l'installation d'un Wordpress sur des infrastructures Windows Server par utilisation d'Ansible et de rôles Yaml.

Une *tour ansible* sous debian gère l'administration des serveurs Windows grâce à *WinRM*.



### Fonctionnement :

Le Playbook principal, *install-complete.yml*, permet la mise en place des rôles : *MariaDB*, *Apache*, *PHP*, *Wordpress*, *Python*.
Chacun des rôles peut être joué de façon indépendante, il suffit de décommenter 3 lignes dans le *main.yml* du dossier *Tasks*.
(se référer au README.md de chaque rôle pour plus de précisions).

Un script Python, *modcreadoss.py*, permet de récupérer les noms d'utilisateurs de l'Active Directory du serveur Windows pour leurs créer un dossier personnel.
(Dans mon cas, je récupère les utilisateurs de deux Unités Organisationnelles *PROFS* et *ELEVES*, mais cela peut être facilement modifié pour l'adapter au besoin).

Erreurs ignorées à signaler : si on rejoue le Playbook plusieurs fois, 4 erreurs sont ignorées :

_ROLE MariaDB :_
* Création de la databse : Elle existe déjà -> *Ignoré*
* Création Admin de la Databse : Il existe déjà -> *Ignoré*

_ROLE Apache :_
* Création Service Apache : Il existe déjà -> *Ignoré*
* Lancement Service Apache : Il est déjà lancé -> *Ignoré*



### Environnement testé :
Pour écrire ce playbook et ses rôles, j'ai utilisé une VM Debian 10 avec Ansible et une VM Windows Server 2016.
Le lien entre Ansible et Windows Server se fait par WinRM.
Dans ma version de Windows Server, la dernière version de VCREDIST a été installé. (nécessaire pour le service Apache)



### Lancement :

- se placer dans le dossier "roles"
- Lancer la commande :
	*sudo ansible-playbook install-complete.yml*


### Données à retenir (information à renseigner pour WORDPRESS):
- Nom de la base de données : Distribution

- Administrateur MARIADB : root
- Mot de passe : root

- Utilisateur privilégié de la base de données : admin
- Mot de passe : admin

- Port : par défaut



### Exemple de *modcreadoss.py* : 

```Python

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

```



### TODO

- Variabilisation afin d'augmenter la modularité.
- Ecrire les Tests.
- Corriger le bug de PHP dans la Path.
- Optimiser/nettoyer les répertoires de travail du playbook.
- Outils de désinstallation/nettoyage des éléments mis en place par la playbook. (Restauration à l'état d'origine)
- Gérer les droits de partage sur les dossiers utilisateurs créés.



#### Par Michaël D. (Kanis66) - le 29/01/2021 - OPENCLASSROOM - Parcours AIC