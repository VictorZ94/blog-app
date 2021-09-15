# WebApp Blog

![](https://img.shields.io/badge/Building-Process-green) ![](https://img.shields.io/badge/Python3-Django-brightgreen)

# Environment

- OS linux - Ubuntu 18.04
- Python 3.6+
- Django 3.2.5.
- PostgreSQL 12.8

# Before run

- execute the Application isolated with virtualenv python3.

    ### Install pip first
    ```Bash
    sudo apt-get install python3-pip
    ```

    ### Then install virtualenv using pip3
    ```Bash
    sudo pip3 install virtualenv
    ```

    ### Now create a virtual environment
    ```Bash
    virtualenv Blog 
    ```

    ### Active your virtual environment
    ```Bash
    source Blog/bin/activate
    ```

    ### move inside Blog virtualenv
    ```Bash
    cd Blog
    ```

    ### clone the project from github page
    ```Bash
    git clone https://github.com/VictorZ94/blog-app.git
    ```


Now you have all environment ready to getting started work with it.

- Create DB:
    ### move inside blog-app
    ```Bash
    cd blog-app
    ```
    Now you'll see your prompt look like. `blog-app$`

    ### install requirements
    ```Bash
    blog-app$ pip3 install -r requirements
    ```

    ### type the next command in prompt console command
    ```Bash
    blog-app$ cat DB.sql | psql -U postgres -W 
    ```
    it creates the DB to get all about models.

- setting your environ viariables.
    ### move inside folder blogApp
    ```Bash
    blog-app$ cd blogApp
    ```

    ### create and open a file call .env
    ```Bash
    blog-app$ vim .env
    ///////////// password and port //////////
    PASSWORD='yourpwd'
    PORT=5433
    ```

    to know port of postgres use:
    ```Bash
    blog-app$ sudo service postgresql status
    10/main (port 5433): online
    ```

    Note PASSWORD and PORT are examples. your credential can be different.

return to the previous folder.
```Bash
cd ..
```

- Migrations

    ## run the command to create tables models of Django
    ```Bash
    blog-app$ python3 manage.py makemigrations 
    ```

    ## run the command to create models into DB
    ```Bash
    blog-app$ python3 manage.py migrate 
    ```

## Fixtures
- [Optional] can be upload data contains in folder fixtures

    ```Bash
    blog-app$ python3 manage.py loaddata fixtures/data_fixture.json
    ```

## Run Blog App

```Bash
blog-app$ python3 manage.py runserver
```

Django use by default port 8000, if you want change it to the port 3000 instead or whatever. type will.

```Bash
blog-app$ python3 manage.py runserver 3000
```

Now open your preferred browser and type the http address.
```Bash
blog-app$ http://localhost:3000/
```

## Usage

Once into app in web. It'll ask you a login. you have 2 options:

1. if you used fixtures mentioned previously there're some users available in the file `MOCK_DATA.json` use them for test the WebApp Blog.

    - Open a file and choices whatever.
    - take username and password.
    - copy and paste in the login.
    - choice one admin and one standard

    note you'll know which is admin because there'll have
     a field called is_admin into `MOCK_DATA.json`.

2. create your own user clicking in sign up.

    - provide the data required.
    - use your username and password to get login

