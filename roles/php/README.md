# PHP
## Mise en place de PHP sur un serveur Windows.



### Descriptif :

Installation de PHP sur un système Windows par Ansible.



### Lancement :

- se placer dans le dossier "roles/php/tasks"
- Modifier le script du fichier *main.yml* comme dans l'exemple ci-dessous (décommenter 3 lignes).
- Lancer la commande :
	*sudo ansible-playbook main.yml*



### Exemple de *main.yml* : 

```
---
# Tache d'installation PHP
- name: Installation PHP
  hosts: windows

  tasks:

    - name: Creation du repertoire php
      win_command: cmd.exe /e:ON mkdir -p c:\php

    - name: Copie php
      win_copy:
        src: /home/ansible/git/Factory/roles/php/files/
        dest: C:\php\
        force: yes

    - name: Decompression zip
      win_command: powershell.exe Expand-Archive -Force c:\php\php-7.4.4-Win32-vc15-x64.zip c:\php

    - name: Mise en place de httpd.conf
      win_copy:
        src: C:\php\httpd.conf
        dest: C:\Apache24\conf\
        remote_src: yes
        force: yes
 
    - name: Ajout de php dans le path
      win_path:
         elements: C:\php\
         state: present

    - name: Arret service Apache
      win_command: powershell NET STOP Apache

    - name: Demarrage service Apache
      win_command: powershell NET START Apache

```


#### Par Michaël D. (Kanis66) - le 29/01/2021 - OPENCLASSROOM - Parcours AIC