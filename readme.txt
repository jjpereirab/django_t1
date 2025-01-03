https://platzi.com/cursos/django/

- Creacion de python env y posterior instalación de ultima version de Django
- Arquitectura MVT, model-view-template, como estructura de desarrollo web en django


Clase 1 - video 5 - Introducción a Modelos y Bases de Datos
-----------------------------------------------------------

1. crear proyecto con django-admin startproject <name> 
2. crear app en project_folder/ con python manage.py startapp <name>
3. en project/project/settings.py agregar el nombre de la app en INSTALLED_APPS
4. crear carpetas "templates/app_folder" dentro de app_folder/, osea app_folder/templates/app_folder/
5. crear html en templates/app_folder
6. crear Vista en views y renderizar el html en ella
7. crear una url en urls y pasarle la Vista



Clase 2 - video 6 - Gestión de Modelos y Bases de Datos en Django con SQLite
----------------------------------------------------------------------------

- Tablas y dbshell
- Django ORM, object-relational mapping, una conexion entre bases de datos y objetos de python
- Comandos migrate y makemigration en manage.py

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

tarea, agregar atributo color a Carro y guardar instancias en base de datos
---
1. instancia Carro(title="marca",year="año") guardada, db modificada 
2. nuevo atributo color agregado, makemigrations y migrate
3. nuevas instancias de Carro guardadas


Clase 4 - video 8 - Actualización y Eliminación de Datos en Django
------------------------------------------------------------------

1. en la dbshell se ven las tablas con .tables, admite sql syntax, mostrando la tabla en terminal con:
	select * from first_app_carro;
2. a una instancia creada en la shell se le pueden modificar sus atributos, y luego de guardados con .save() los cambios se verán en la dbshell
3. la instancia se puede tambien eliminar en la shell con .delete()

nota
---
makemigrations y migrate es necesario al crear nuevos modelos y/o modificar sus atributos, no fue necesario al modificar el metodo __str__()



