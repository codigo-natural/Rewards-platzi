# PLATZI PREMIOS

Estructura de carpetas de un proyecto con Django
[Estructura de carpetas de un proyecto con Django](https://studygyaan.com/wp-content/uploads/2019/07/Best-Practice-to-Structure-Django-Project-Directories-and-Files.png)

- El archivo "manage.py" es el archivo principal que se utiliza para interactuar con el proyecto de Django y realizar tareas como la creación de aplicaciones, la ejecución de pruebas y la administración de la base de datos.

> diagrama entidad-relacion del proyecto
# Espacio Trabajo

## Pag. Tools Web

---

[Algoritmos](https://www.notion.so/Algoritmos-4cb88a35678043689b272b7d89d70571)

[Lofi.co - Craft your focus environment](https://app.lofi.co/)

[SAVEE](https://savee.it/)

[OpenAI API](https://beta.openai.com/)

[DALL·E](https://labs.openai.com/)

[React Projects || John Smilga](https://www.notion.so/React-Projects-John-Smilga-61c597bbfb0a4bdcb6daab572c6d3929)

[php Laravel](https://www.notion.so/php-Laravel-11b399a61cd4468d8ce25c2ad30075e5)

[](https://source.unsplash.com/random)

[Snappr Photography | Powering the internet's photos](https://www.snappr.com/)

[pattern.css - Background Patterns in CSS](https://www.notion.so/pattern-css-Background-Patterns-in-CSS-888ea0ae07704f91814d1122f42546f4)

[Plantillas charlas tecnicas](https://www.notion.so/Plantillas-charlas-tecnicas-c8ab9f7b79334256a0e3750cbef2b02f)

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