from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.urls import reverse

# Create your views here.
def index(request):
    todos = Todo.objects.all() 
    content = { 'todos': todos }
    return render(request, 'app1/index.html', content) 

def create_todo(request):
    a= request.POST['todoContent']
    Todo(content = a).save() 
    return HttpResponseRedirect( reverse('index') )

def delete_todo(request):
    a= request.GET['todoNum']
    Todo.objects.get( id =a ).delete() 
    return HttpResponseRedirect( reverse('index') )

    