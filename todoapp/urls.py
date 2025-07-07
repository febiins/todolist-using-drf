from django.urls import path
from .views import todo_list,todo_detail
from . import views

urlpatterns = [

     path('todos/', views.todo_list,name="todo_list"),
     path('todos/<int:pk>/', views.todo_detail,name="todo_detail"),
]