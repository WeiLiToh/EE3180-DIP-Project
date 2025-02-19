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
* 1. Run the command "pip install -r requirements.txt" to install all python packages required for the website.
* 2. Create .env file in EE3180-DIP-Project folder.
* 3. Make the following changes to the .env file:
![image](https://github.com/user-attachments/assets/96a1c9ac-e71a-4cde-bad0-fd2e58b942ef)
* MYSQL_Host --> localhost
* MYSQL_User --> default root
* MYSQL_PASSWORD --> Your selected password
* MYSQL_DB --> Name of your database in MySQL Workbench
* Open up a terminal and ensure that "mainapp.py" is in your current working directory.
* Run the command "python mainapp.py"

```
code blocks for commands
```

## Help

Update database name in views.py
```
![image](https://github.com/user-attachments/assets/cf67a8c7-537c-4742-a9e7-f6dba3f257b6)
```
