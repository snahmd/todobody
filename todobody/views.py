from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
from.serializers import TodoSerializer 
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView 


# Create your views here.
def Home(request):
    return HttpResponse("TODOBODY")


class Todos(ListCreateAPIView):
    queryset = Todo.objects.filter(is_done=False)
    serializer_class = TodoSerializer  

class TodoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.filter(is_done=False)
    serializer_class = TodoSerializer        