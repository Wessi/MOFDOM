
## Mofedmain: Dynamic web app for regional finance bureaus

## Brief Description**

This web-based system is developed for MOFED (Ministry of Finance and Economic Development) to be implemented by all regional finance bureaus. It features dynamic pages allowing each bureau to have unique content and data uploaded by their designated administrators.

# Table of Contents

# Technology Stack:
# Dependencies: 
# Getting Started: 
# Running the Project: 
# Branching :
--------------------------------------------

# Technology Stack

The following are the core technologies used to build the application.

* Back-end: Django (a Python web framework)
* Front-end: HTML, CSS, JavaScript, Bootstrap (web development technologies)
* Database: Default is Sqlite3 which will be automatically created if no other database is configured. You Can also use any relational database  like PostgreSQl or MySQL





# Prerequisites and Dependencies
    Operating System: System has been tested on windows 10, Windows 11 and linux operating system. Since the project is developed using Django
    and it's dependencies theoretically it should be running in all operating systems including windows, linux, mac.

    Python version >= 3.8: Ensure you have the required Python version installed on your system. You can check the version by running `python --version` in your terminal.
    
    Other dependencies: All additional libraries required for the project are listed in the `requirements.txt` file and will be installed in following steps.





# Getting Started 

Follow the following steps to set up the development environment for your project.    

 ## Cloning the Repository to your local machine:
    * Use the provided command to download the project's codebase from GitHub.
    
    ```bash
    git clone https://github.com/Sevenstar-A/Mofedmain.git
    ```

 ## Setting Up the Environment

    ## Create a virtual environment
        * This step isolates project dependencies from your system-wide Python installations.
        ```bash
        $ python -m venv venv
        ```
    ## Activate the virtual environment
        ```bash
        $ source venv/Scripts/activate
        ```

## Install dependencies
    
    This command installs all the required libraries listed in `requirements.txt` into your activated virtual environment.
    ```bash
        $ pip install -r requirements.txt
    ```
    

# Running the Project 

This section explains how to launch the development server and access your application locally.

## Database Migrations
    * These commands are essential for creating the database schema based on your project's models.
        * `makemigrations`: Analyzes your models and generates migration files.
       
        ``` bash
        $ py manage.py makemigrations about_us accounts blogs core dashboard documents news suppliers task_manager vacancies
        ```

        * `migrate`: Applies the generated migrations to your database.
        ``` bash
        $ python manage.py migrate
        ```
            
        ## Then check if migration files are created in all apps. In some cases, the makemigrations command might not generate migration files for some app. If such thing happens, use the following command to add the name of apps whose migration files are not generated

        ``` bash
        $ python manage.py makemigrations about_us accounts blogs core etc (list names of apps)

        ```
    
    ## Notes:
    * You can remove all the data from the databases and return to an empty state using the:
    ```bash
    $ python manage.py flush
    ```

    * The default database is Sqlite3 which will be generated when you run migration commands. You can configure any relational database supported by Django which includes PostgreSQL and MySQL. 
    Configuration of PostgreSQL:
    - Open the settings.py file and replace the default database setting for Sqlite with the following PostgreSQL conf replacing your database credentials
    
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': $Your_DB_Name,
        'USER': $Your_DB_Username,
        'PASSWORD': $Your_DB_Password,
        'HOST': '127.0.0.1',
        'PORT': 5432,
    }
    For further reading on how to install MySql and integrate with Django use the following blog.
    
    
    Configuration of MySQL, 
    - Open the settings.py file and replace the default database setting for Sqlite with the following MySQL conf replacing your database credentials
    
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        ' NAME': $Your_DB_Name,
        'USER': $Your_DB_Username,
        'PASSWORD': $Your_DB_Password,
        'HOST':'localhost',
        'PORT':'3306',
    }

    For further reading on how to install MySql and integrate with Django use the following blog.
    https://www.geeksforgeeks.org/how-to-integrate-mysql-database-with-django/




##  To create a superuser account, use this command and fill in the required fields:

```bash
$ python manage.py createsuperuser
```

## Starting the Development Server
    * Run this command to launch the built-in Django development server.
    ```bash
    $ python manage.py runserver
    ```

## Access the application
    * You can then access your application by opening http://127.0.0.1:8000/ in your web browser.
    * Access website : http://127.0.0.1:8000/

    Login page url:
    http://127.0.0.1:8000/accounts/login/

    After Login
    * Access for internal dashboard
    http://127.0.0.1:8000/dashboard/

    * Access for admin
    http://127.0.0.1:8000/admin/


# Deployment:
The web app can be deployed on any hosting platform that supports Python. These include AWS, Azure, Heroku, Pythonanywhere, and VPS (Linux and Windows). Deployment instructions can have some specific differences based on the deployment platform. 

# Branching:
As a git repo, our repo will follow the common branching strategies. There are 3 main categories, the master, development, and feature branches.
1. The master branch is the deployment branch, which will only contain stable versions that will be used for deployment purposes
2. The dev branch is the development branch, which is actively being updated and/or merged with feature branches hence having the latest updates from all. Any individual who wants to trach the development of the system should continuously pull from the dev branch
3. The other branches are feature branching which are intended to update specific features of the system. After they are completed they will be merged with the dev branch.
 
