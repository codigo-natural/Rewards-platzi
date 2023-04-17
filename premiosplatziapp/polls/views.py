# Importando las funciones necesarias de Django
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Importando los modelos de nuestra aplicación "polls"
from . models import Question, Choice

def index(request):
  # Obteniendo todas las preguntas de nuestra base de datos
  latest_question_list = Question.objects.all()
  # Renderizando la plantilla "polls/index.html" y pasándole como contexto
  # la lista de preguntas obtenidas anteriormente
  return render(request, 'polls/index.html', {
    'latest_question_list': latest_question_list
  })

def detail(request, question_id):
  # Obteniendo la pregunta correspondiente al ID proporcionado o devolviendo un error 404 en caso de que no exista
  question = get_object_or_404(Question, pk=question_id)
  # Renderizando la plantilla "polls/detail.html" y pasándole como contexto
  # la pregunta obtenida anteriormente
  return render(request, 'polls/detail.html', {
    'question': question
  })

def results(request, question_id):
  # Devolviendo una respuesta HTTP con un mensaje que indica el número de pregunta que se está visualizando
  return HttpResponse(f'Estas viendo los resultados de la pregunta número {question_id}')

def vote(request, question_id):
  # Obteniendo la pregunta correspondiente al ID proporcionado o devolviendo un error 404 en caso de que no exista
  question = get_object_or_404(Question, pk=question_id)
  try:
    # Obteniendo la opción seleccionada por el usuario a través de una petición POST
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    # Si el usuario no ha seleccionado ninguna opción, volvemos a mostrar la página de detalle de la pregunta con un mensaje de error
    return render(request, "polls/detail.html", {
      "question": question,
      "error_message": "No elegistes una respuesta"
    })
  else:
    # Añadiendo un voto a la opción seleccionada por el usuario y guardando los cambios
    selected_choice.votes += 1
    selected_choice.save()
    # Redireccionando al usuario a la página de resultados de la pregunta
    return HttpResponseRedirect(reverse("poll:results", args=(question.id,)))
  