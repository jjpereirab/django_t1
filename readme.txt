https://platzi.com/cursos/django/

creacion de python env y posterior instalación de ultima version de Django
arquitectura MVT, model-view-template, como estructura de desarrollo web en django


Clase 1 - video 5
-----------------

1. crear proyecto con django-admin startproject <name> 
2. crear app en project_folder/ con python manage.py startapp <name>
3. en project/project/settings.py agregar el nombre de la app en INSTALLED_APPS
4. crear carpetas "templates/app_folder" dentro de app_folder/, osea app_folder/templates/app_folder/
5. crear html en templates/app_folder
6. crear Vista en views y renderizar el html en ella
7. crear una url en urls y pasarle la Vista



Clase 2 - video 6
-----------------

Django ORM, object-relational mapping, una conexion entre bases de datos y objetos de python
comandos migrate y makemigration en manage.py

1. las migraciones pre-existentes se realizan con ./manage.py migrate
2. crear una clase (Carro) en models.py, la cual será una nueva migracion
3. las nuevas migraciones se trackean con ./manage.py makemigrations
4. luego de trackear la migracion, realizarla otra vez con ./manage.py migrate
5. en app_folder/migrations/ se crea un archivo con la clase Carro que tiene un id y un title
6. exploracion de settings.py, particularmente DATABASES
7. comandos .tables y .schema first_app_carro (<app_name>_<model_name>) dentro de ./manage.py dbshell
*. para el paso 7 es necesario sudo apt install sqlite3


Clase 3 - video 7 - Inserción de Datos con Django
-------------------------------------------------

1. crear nuevo atributo (año) en la clase de models.py, como nuevo campo en una tabla
2. makemigrations luego del cambio, solucion del error al crear un nuevo campo que no puede ser nulo por defecto. Agregar nuevo parametro al año (null=True)
3. makemigrations ahora funciona y se puede revisar la nueva migracion en app_folder/migrations/
4. migrate para realizar cambio en la base de datos
5. agregar metodo __str__ al modelo
6. uso de ./manage.py shell, from first_app.models import Carro, instancia de carro=Carro(title="",year="")
7. print(carro), metodo .save() a la instancia para guardar entrada en la base de datos
