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



### Lancement :

- se placer dans le dossier "roles"
- Lancer la commande :
	*sudo ansible-playbook install-complete.yml*



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



#### Par Michaël (Kanis66) - le 29/01/2021