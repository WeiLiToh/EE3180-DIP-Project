# EE3180 DIP: SQL Attacks and Prevention 

This project aims to replicate known SQL attacks on a vulnerable database in order to exfiltrate privileged information as a low level operator. 

## Description

<Include usage of SQL attacks after completion>

## Getting Started

### Dependencies

* Visual Studio Code, MySQL Workbench

### Executing program

* Github Desktop Setup:
* 1. Accept invitation for collaboration on Github repository
* 2. Github desktop should autopopulate with this project repository
* 3. Select clone repository locally (Recommend choosing your desktop for file path)

* MySQL Workbench:
* 1. Create new SQL connection
* 2. Create new database (e.g. CREATE DATABASE testdb)

* Running the website:
* 1. Create a virtual environment "python -m venv venv"
* 2. Activate a virtual environment "venv\Scripts\activate" 
* 3. Run the command "pip install -r requirements.txt" to install all python packages required for the website.
* 4. Create .env file in EE3180-DIP-Project folder.
* 5. Make the following changes to the .env file:
![image](https://github.com/user-attachments/assets/96a1c9ac-e71a-4cde-bad0-fd2e58b942ef)
* MYSQL_Host --> localhost
* MYSQL_User --> default root
* MYSQL_PASSWORD --> Your selected password
* MYSQL_DB --> Name of your database in MySQL Workbench
* Open up a terminal and ensure that "mainapp.py" is in your current working directory.
* Run the command "python mainapp.py"

```
code blocks for commands!

```

## Help

1. Unable to activate virtual environment due to security error --> "Set-ExecutionPolicy Unrestricted -Scope Process"
2. In views.py --> Update user, password, database name. 

![changing database name_views](https://github.com/user-attachments/assets/71eb4ded-23cb-4423-bd54-c49cee01bfa2)

```

```

# Possible Attack Tools
SQLmap

Example command: sqlmap.py -u "http://127.0.0.1:5000" --cookie="session=.eJwljjkOwzAMwP7iuYNkS3KUzwS2DrRr0kxF_94UGQkCBD9lyz2OZ1nf-xmPsr28rCX7TE9I5UoZTIk2GZObuYUsxBMyOYKM1bwZj9oBG8Mkdq-2kKBEsKdexGKdKGBgasXxjyUKQrZQGThparNQ7U6XEgEr18h5xH7fYPn-AFufMLk.Z7WSwA.U_tWC-N7OVAcQhJo9GRDxW-DKSA" --batch --dbs --crawl=3 --forms --level=5 --risk=3

![image](https://github.com/user-attachments/assets/04ac003a-170e-4cb0-8b9c-d4bbe124c502)



