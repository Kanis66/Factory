# MariaDB
## Mise en place de MariaDB sur un serveur Windows.



### Descriptif :

Installation de MariaDB sur un système Windows par Ansible.



### Lancement :

- se placer dans le dossier "roles/mariadb/tasks"
- Modifier le script du fichier *main.yml* comme dans l'exemple ci-dessous (décommenter 3 lignes).
- Lancer la commande :
	*sudo ansible-playbook main.yml*



### Exemple de *main.yml* : 

```
---
# Tache d'installation Apache
- name: Installation MariaDB MSI
  hosts: windows

  tasks:
    - name: Creation du repertoire MariaDB
      win_command: cmd.exe /e:ON mkdir -p c:\mariadb 

    - name: Copie MariaDB
      win_copy:
        src: /home/ansible/git/Factory/roles/mariadb/files/
        dest: C:\mariadb\
        force: yes

    - name: Install MariaDB
      win_command: C:\windows\system32\msiexec.exe /i c:\mariadb\mariadb-10.5.4-winx64.msi SERVICENAME=MariaDB PASSWORD=root /qn
      ignore_errors: yes

    - name: Creation de la base de données
      win_command: mysql.exe --host=localhost --user=root --password=root -e "CREATE DATABASE Distribution"
      ignore_errors: yes
      args:
        chdir: c:\Program Files\MariaDB 10.5\bin\

    - name: Creation admin de database
      win_command: mysql.exe --host=localhost --user=root --password=root -e "CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin'"
      ignore_errors: yes
      args:
        chdir: c:\Program Files\MariaDB 10.5\bin\

    - name: Attribution des droits
      win_command: mysql.exe --host=localhost --user=root --password=root -e "GRANT ALL PRIVILEGES ON Distribution.* TO 'admin'@'localhost'"
      args:
        chdir: c:\Program Files\MariaDB 10.5\bin\

```



#### Par Michaël D. (Kanis66) - le 29/01/2021 - OPENCLASSROOM - Parcours AIC