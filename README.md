# WebApp Blog

![](https://img.shields.io/badge/Building-Process-green) ![](https://img.shields.io/badge/Python3-Django-brightgreen)

## Ambiente de ejecución

- OS linux - Ubuntu 18.04
- Python 3.6+ o superior.
- Django 3.2.5.
- PostgreSQL 12.8

## Antes de ejecutar la app

- Crea la base datos:
    - Corre el siguiente comando
    ```Bash
    blogApp$ cat DB.sql | psql -U postgre -W 
    ```
    Esto creara la base de datos para recibir todos los modelos

- Ejecuta el comando de `makemigrations` de Django, crea la nuevas migraciones de tus modelos

    ```Bash
    blogApp$ python3 manage.py makemigratios 
    ```
    Asegurate de estar dentro de tu proyecto para correrlo

- Por último corre el comando para crear tus modelos dentro de la base de datos

    ```Bash
    blogApp$ python3 manage.py migrate 
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
