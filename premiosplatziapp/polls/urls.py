from django.urls import path

from . import views
# Lista de rutas URL que el servidor Django puede manejar
urlpatterns = [
    # Ruta para la página de inicio, con una vista llamada "index"
    path("", views.index, name="index"),
    # Ruta para la vista de detalle de una pregunta, 
    # con una vista llamada "detail" y un parámetro de int llamado "question_id"
    path("detail/<int:question_id>", views.detail, name="detail"),
    # Ruta para la vista de resultados de una pregunta,
    # con una vista llamada "results" y un parámetro de int llamado "question_id"
    path("results/<int:question_id>", views.results, name="results"),
    # Ruta para la vista de votación de una pregunta, 
    # con una vista llamada "vote" y un parámetro de int llamado "question_id"
    path("vote/<int:question_id>", views.vote, name="vote"),
]