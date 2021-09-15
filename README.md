# WebApp Blog

![](https://img.shields.io/badge/Building-Process-green) ![](https://img.shields.io/badge/Python3-Django-brightgreen)

## Ambiente de ejecución

- OS linux - Ubuntu 18.04
- Python 3.6+ o superior.
- Django 3.2.5.
- PostgreSQL 12.8

## Antes de ejecutar la app

- Crea la base de datos:
    - Corre el siguiente comando
    ```Bash
    blogApp$ cat DB.sql | psql -U postgre -W 
    ```
    Esto creara la base de datos para recibir todos los modelos.
    Nota: guarda la contraseña de tu DB en un archivo .env `PASSOWRD=your_password` y el puerto al cual te conectarás `PORT=543*`  dentro de la carpeta blogApp en donde está settings.py 

- Ejecuta el comando de `makemigrations` de Django, crea la nuevas migraciones de tus modelos

    ```Bash
    blogApp$ python3 manage.py makemigratios 
    ```
    Asegurate de estar dentro del proyecto blogApp o como sea lo hayas nombrado para correrlo

- Por último, corre el comando para crear los modelos dentro de la base de datos

    ```Bash
    blogApp$ python3 manage.py migrate 
    ```

#### !importante
- [Opcional] puedes cargar los datos contenidos en la carpeta fixtures.

    ```Bash
    blogApp$ python3 manage.py loaddata fixtures/data_fixture.json
    ```


## Ejecutar la app

```Bash
blogApp$ python3 manage.py runserver
```

django usa por defecto el puerto 8000.
si quieres cambiarlo al puerto 3000 o cualquera, corre lo siguiente.

```Bash
blogApp$ python3 manage.py runserver 3000
```

Ahora ingresa al navegador y entra la dirección http.
```Bash
blogApp$ http://localhost:3000/
```

## Uso de la App

Cuando ingreses al navegador y escribas la dirección `http://localhost:3000/` automáticamente de redireccionará al login para autenticarte. Una vez aquí tienes 2 opciones:

1. si cargaste los fixtures anterior tienes algunos usuarios disponibles en el archivo `MOCK_DATA.json`para testear la APP

    - Abre el archivo y elije cualquier usuario
    - toma el username y password.
    - ingresalos en el login

![Usuarios disponibles](https://i.imgur.com/z3A8JAa.png)
