This is a web based system developed for MOFED in order to be implemented by all regional finance bureaus. It contains  
--------------------------------------------

# Running the Project Locally

## First, clone the repository to your local machine :

```bash
git clone https://github.com/Sevenstar-A/Mofedmain.git
```

## Create a virtual environment :

```bash
$ python -m venv .venv
```

## Activate the virtual environment:


```bash
$ source venv/Scripts/activate
```

## Install the requirements :

```bash
$ pip install -r requirements.txt
```


## Generate migration files for all apps
``` bash
$ python manage.py makemigrations

```


## Apply the migrations :
``` bash
$ python manage.py migrate
```

## Then check if migration files are created in all apps
## In some cases, the makemigrations command might not generate migration files for some app, 
## If such thing happens, use the following command to add the name of apps whose migration files are not generated

``` bash
$ python manage.py makemigrations about_us accounts blogs core etc (list names of apps)

```


## To create another superuser account, use this command:

```bash
$ python manage.py createsuperuser
```


## If you are on deployment server, Run collect static :

```bash
$ python manage.py collectstatic
```



## Finally, run the development server :

```bash
$ python manage.py runserver
```

<b>The project will be available at :   </b>  **http://localhost:8000**



## Notes:
* You can remove all the data from the databases and return to an empty state using the:
```bash
$ python manage.py flush
```
