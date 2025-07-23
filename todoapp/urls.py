from django.urls import path
from .views import todo_list,todo_detail
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

     path('todos/', views.todo_list,name="todo_list"),
     path('todos/<int:pk>/', views.todo_detail,name="todo_detail"),
     path('api-token-auth/', obtain_auth_token),
]