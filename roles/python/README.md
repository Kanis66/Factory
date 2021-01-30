# Python
## Mise en place de Python sur un serveur Windows.



### Descriptif :

Installation de Python sur un système Windows par Ansible.



### Lancement :

- se placer dans le dossier "roles/python/tasks"
- Modifier le script du fichier *main.yml* comme dans l'exemple ci-dessous (décommenter 3 lignes).
- Lancer la commande :
	*sudo ansible-playbook main.yml*



### Exemple de *main.yml* : 

```
---
# Tache installation python
- name: Installation python
 hosts: windows

 tasks:
    - name: Creation du repertoire python
      win_command: cmd.exe /e:ON mkdir -p c:\python

    - name: Copie python et module
      win_copy:
        src: /home/ansible/git/Factory/roles/python/files/
        dest: C:\python\
        force: yes


    - name: Installation Python
      raw: 'c:\python\python-3.9.1-amd64.exe /quiet /passive InstttallAllUsers=1 PrependPath=1 Include_test=1 Include_pip=1 Include_lib=1 Include_dev=1 Include_tools=1'

    - name: Installation module pyad
      raw: 'py -m pip install pyad'

    - name: Installation module pywin32
      raw: 'py -m pip install pypiwin32'

    - name: Lancement module création répertoire
      win_command: py c:\python\modcreadoss.py
      args:
        chdir: c:\

```



#### Par Michaël D. (Kanis66) - le 29/01/2021 - OPENCLASSROOM - Parcours AIC