https://platzi.com/cursos/django/

Clases 1-4
----------

- Creacion de python env y posterior instalación de ultima version de Django
- Arquitectura MVT, model-view-template, como estructura de desarrollo web en django


Clase 5 - Introducción a Modelos y Bases de Datos
-----------------------------------------------------------

1. crear proyecto con django-admin startproject <name> 
2. crear app en project_folder/ con python manage.py startapp <name>
3. en project/project/settings.py agregar el nombre de la app en INSTALLED_APPS
4. crear carpetas "templates/app_folder" dentro de app_folder/, osea app_folder/templates/app_folder/
5. crear html en templates/app_folder
6. crear Vista en views y renderizar el html en ella
7. crear una url en urls y pasarle la Vista


Clase 6 - Gestión de Modelos y Bases de Datos en Django con SQLite
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

nota
''''
Para abrir la dbshell es necesario sudo apt install sqlite3


Clase 7 - Inserción de Datos con Django
-------------------------------------------------

1. crear nuevo atributo (año) en la clase de models.py, como nuevo campo en una tabla
2. makemigrations luego del cambio, solucion del error al crear un nuevo campo que no puede ser nulo por defecto. Agregar nuevo parametro al año (null=True)
3. makemigrations ahora funciona y se puede revisar la nueva migracion en app_folder/migrations/
4. migrate para realizar cambio en la base de datos
5. agregar metodo __str__ al modelo
6. uso de ./manage.py shell, from first_app.models import Carro, instancia de carro=Carro(title="",year="")
7. print(carro), metodo .save() a la instancia para guardar entrada en la base de datos

tarea: agregar atributo color a Carro y guardar instancias en base de datos
'''''
1. instancia Carro(title="marca",year="año") guardada, db modificada 
2. nuevo atributo color agregado, makemigrations y migrate
3. nuevas instancias de Carro guardadas


Clase 8 - Actualización y Eliminación de Datos en Django
------------------------------------------------------------------

1. en la dbshell se ven las tablas con .tables, admite sql syntax, mostrando la tabla en terminal con:
	select * from first_app_carro;
2. a una instancia creada en la shell se le pueden modificar sus atributos, y luego de guardados con .save() los cambios se verán en la dbshell
3. la instancia se puede tambien eliminar en la shell con .delete()

nota
''''
makemigrations y migrate es necesario al crear nuevos modelos y/o modificar sus atributos, no fue necesario al modificar el metodo __str__()


Clase 9 - Creación y Gestión de Relaciones entre Modelos en Django
----------------------------------------------------------------------------

- Campo de fecha models.DateField()
- Atributo de relacion entre tablas, model.ForeignKey()

1. crear nuevos modelos Editor y Libro, y un atributo en Libro que lo relaciona con Editor
2. Libro tiene un atributo de tipo fecha, usando un nuevo tipo de campo de django models.DateField()
3. en este caso el atributo de relacion en Libro tiene un parametro on_delete=models.CASCADE, lo que significa que al borrar un Editor entonces todos sus libros se borrarán tambien. Otros valores de on_delete son DO_NOTHING y PROTECT
4. makemigrations y migrate, y pip install ipython para mejorar la shell
5. crear instancias de Editor y Libro, primero Editor, luego en Libro en el atributo que lo relaciona con editor se pone la instancia recien creada de Editor. i.e.
	edi = Editor(nombre="un nombre", direccion="una direccion")
	edi.save()
	lib = Libro(titulo="un titulo", fecha_publicacion="2024-12-31", editor=edi)
	lib.save()
6. ver en la dbshell

nota
''''
Se relacionó la clase Libro con la clase Editor, de forma "uno a muchos", un editor a muchos libros


Clase 10 - Relaciones Muchos a Muchos (N:N) en Django
---------------------------------------------------------------

- Campo de relacion models.ManyToManyField(Autor, related_name="autores")

1. crear nuevo modelo Autor para la relacion de muchos a muchos con Libros
2. la clase Autor debe estar antes que Libros ya que se *relaciona* en Libros
3. makemigrations y migrate, esto crea una nueva tabla de relaciones entre Libro y Autor
4. abrir la shell y crear instancias de Autor a1 y a2 (guardarlas o luego no se podran relacionar en la db)
5. seleccionar el libro creado en la sesion anterior con:
	lib = Libro.objects.first()
6. asignar los autores a  con:
	lib.autores_atrib.set([a1, a2])
7. ya se puede ver contenido en la tabla de relaciones libro_autores_atrib en la dbshell

nota
''''
Luego del paso 6, si se hace lib.save() se modifica db.sqlite3, pero no pude identificar qué cambió. No hay cambios aparentes en las tablas de libro ni en la de libro_autores_atrib. Entonces, ya se habian creado las relaciones en la tabla libro_autores_atrib, pero aun asi al hacer lib.save() algo mas cambió en la db. 


Clase 11 - Relaciones Uno a Uno (1:1) en Django
---------------------------------------------------------

- Atributo models.URLField()
- Campo de relacion models.OneToOneField()

1. nuevo modelo Perfil para relacionar con Autor, con la relacion 1:1 models.OneToOneField(Autor, on_delete=models.CASCADE), si se borra el autor, se borrará su perfil
2. makemigratios y migrate
3. tomar el primer objeto de Autor y asociarlo a una nueva instancia de Perfil:
	au = Autor.objects.first()
	p = Perfil(website="www.aubrey.com", biografia="la biografia de Aubrey en bio del website", autor=au)
	p.save()
4. ya se puede verificar en la base de datos


Clase 12 - Queries y Filtros en Django: Optimización y Estrategias Avanzadas
----------------------------------------------------------------------------

- Django Managers
	Model.objects.[ count(), first(), last(), all(), get(by_arg), filter(by_arg), create(args), update(args) ]
- para .create(args) se puede usar Model?? en ipython para ver los argumentos
- Model.objects.create(args) guarda la instancia automaticamente, sin necesidad de .save()
- get(by_arg) retorna un objeto, mientras filter(by_arg) retorna una lista 
- A .all() o .filter() que retornan listas, se les puede concatenar .order_by("model_attrib"). e.g.
	Autor.objects.all().order_by("nombre")
	

