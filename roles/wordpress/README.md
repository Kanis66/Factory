# Wordpress
## Mise en place de Wordpress sur un serveur Windows.



### Descriptif :

Installation de Wordpress sur un système Windows par Ansible.



### Lancement :

- se placer dans le dossier "roles/wordpress/tasks"
- Modifier le script du fichier *main.yml* comme dans l'exemple ci-dessous (décommenter 3 lignes).
- Lancer la commande :
	*sudo ansible-playbook main.yml*



### Exemple de *main.yml* : 

```
---
# Tache de mise en place de wordpress
- name: Installation wordpress
  hosts: windows

  tasks:
    - name: Creation du repertoire WP
      win_command: cmd.exe /e:ON mkdir -p c:\wp

    - name: Copie Wordpress
      win_copy:
        src: /home/ansible/git/Factory/roles/wordpress/files/
        dest: C:\wp\
        force: yes


    - name: Decompression zip
      win_command: powershell.exe Expand-Archive -Force c:\wp\wordpress-5.6-fr_FR.zip c:\

    - name: Mise a jour httpd.conf
      win_copy:
        src: C:\wp\httpd.conf
        dest: C:\Apache24\conf
        remote_src: yes
        force: yes
    
    - name: Arret service Apache
      win_command: powershell NET STOP Apache

    - name: Demarrage service Apache
      win_command: powershell NET START Apache

```



#### Par Michaël D. (Kanis66) - le 29/01/2021 - OPENCLASSROOM - Parcours AIC