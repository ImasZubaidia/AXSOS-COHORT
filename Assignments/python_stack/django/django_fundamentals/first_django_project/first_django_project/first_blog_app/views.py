from email import message
from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse

def root(request):
    return redirect('/blogs')

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/')

def show(request,number):
    message="placeholder to display blog number:"+str(number)
    return HttpResponse(message)

def edit(request,number):
    message="placeholder to edit blog "+str(number)
    return HttpResponse(message)

def destroy(request,number):
    return redirect('/blogs')

def json(request):
    return JsonResponse({"title": "my first blog app", "content": "Lorem, ipsum dolor sit amet consectetur adipisicing elit."})