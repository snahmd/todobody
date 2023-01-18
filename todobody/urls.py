from django.contrib import admin
from django.urls import path, include
from .views import Home, Todos, TodoDetail

urlpatterns = [
    
    path("", Home ),
    path("todo", Todos.as_view()),
    path("todo/<int:pk>", TodoDetail.as_view())
]