from urllib import request
from django.shortcuts import render,redirect

def index(request):
    return render(request,"index.html")

def create_user(request):

    print("Got Post Info....................")
    name_on_template = request.POST['name'] 
    location_on_template = request.POST['dojo_location']  
    language_on_template = request.POST['favorite_language']
    comment_on_template = request.POST['comment']

    print(name_on_template)
    print(location_on_template)
    context = {
    "name_on_template" : name_on_template,
    "location_on_template" : location_on_template,
    "language_on_template":language_on_template,
    "comment_on_template":comment_on_template

    }
    return render(request,"result.html",context)
print(dir(request))

def go_back(request):
    return redirect('/')