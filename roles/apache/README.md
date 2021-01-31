# Apache
## Mise en place d'Apache sur un serveur Windows.



### Descriptif :

Installation d'un serveur Apache sur un système Windows par Ansible.



### Lancement :

- se placer dans le dossier "roles/apache/tasks"
- Modifier le script du fichier *main.yml* comme dans l'exemple ci-dessous (décommenter 3 lignes).
- Lancer la commande :
	*sudo ansible-playbook main.yml*



### Exemple de *main.yml* : 

```
---

# Tache d'installation Apache
- name: Installation Apache MSI
  hosts: windows

  tasks:
  - name: Creation du repertoire Apache
    win_command: cmd.exe /e:ON mkdir -p c:\apache 

  - name: Copie Apache
    win_copy:
      src: /home/ansible/git/Factory/roles/apache/files/
      dest: C:\apache\
      force: yes

  - name: Decompresse Apache
    win_command: powershell.exe Expand-Archive -Force C:\apache\httpd-2.4.43-win64-VS16.zip C:\

  - name: Configuration Apache
    win_copy:
      src: c:\apache\httpd.conf
      dest: c:\Apache24\conf\
      remote_src: yes
      force: yes

  - name: Installation service Apache
    win_command: httpd.exe -k install -n "Apache"
    ignore_errors: yes
    args:
      chdir: c:\Apache24\Bin\

  - name: Parametrage service Apache
    win_command: powershell Set-Service -Name Apache -StartupType Automatic

  - name: Demarrage service Apache
    win_command: powershell NET START Apache
    ignore_errors: yes


```



#### Par Michaël D. (Kanis66) - le 29/01/2021 - OPENCLASSROOM - Parcours AIC