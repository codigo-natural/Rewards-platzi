# PLATZI PREMIOS

Estructura de carpetas de un proyecto con Django
[Estructura de carpetas de un proyecto con Django](https://studygyaan.com/wp-content/uploads/2019/07/Best-Practice-to-Structure-Django-Project-Directories-and-Files.png)

- El archivo "manage.py" es el archivo principal que se utiliza para interactuar con el proyecto de Django y realizar tareas como la creación de aplicaciones, la ejecución de pruebas y la administración de la base de datos.

> diagrama entidad-relacion del proyecto

**questions**

| id | int |
| --- | --- |
| question_text | varchar |
| pub_date | datetime |

**choices**

| id | int |
| --- | --- |
| question | int |
| choice_text | varchar |
| votes | int |

**Comando para acceder a la consola interactiva de Django:** 
> py manage.py shell
```python      
# Importacion de los modelos
from polls.models import Question, Choice


# Llamado de todos los registros de un modelo
Question.objects.all()

# funcion para crear objetos de tipo date_time(timezone)
from django.utils import timezone

# Creacion de un nuevo registro
q = Question(question_text="¿Cual es el mejor curso de Platzi?", pub_date=timezone.now())

# Guardado del nuevo registro
q.save()
```