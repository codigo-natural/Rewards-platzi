# Importando las funciones necesarias de Django
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
# Importando los modelos de nuestra aplicación "polls"
from . models import Question, Choice
class IndexView(generic.ListView):
  # Definimos el nombre de la plantilla que se utilizará para la vista
  template_name = 'polls/index.html'
  # Definimos el nombre del objeto que se utilizará para representar la lista de objetos que se mostrarán en la vista
  context_object_name = 'latest_question_list'

  def get_queryset(self):
    """Return the last five published questions"""
    # Selecciona las últimas cinco preguntas y las ordena por fecha de publicación descendente
    return Question.objects.order_by('-pub_date')[:5]
class DetailView(generic.DetailView):
    # Definimos el modelo que se utilizará para la vista
    model = Question
    # Definimos el nombre de la plantilla que se utilizará para la vista
    template_name = "polls/detail.html"
class ResultView(DetailView):
    # Definimos el nombre de la plantilla que se utilizará para la vista
    template_name = "polls/results.html"

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
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
  