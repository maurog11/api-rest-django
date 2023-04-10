from django.urls import path
from . import views

# Devuelve una lista de personas en formato JSON
urlpatterns = [
    path('personas/', views.PersonListView.as_view()),
    path('personas/', views.PersonListView.as_view()),
    path('tareas/', views.TaskListView.as_view()),
    path('tareas/', views.TaskListView.as_view()),
]