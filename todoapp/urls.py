from django.urls import path
from .views import todo_list
from . import views

urlpatterns = [

     path('todos/', views.todo_list),
]