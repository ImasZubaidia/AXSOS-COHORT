from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book, User

def index(request):
    return render(request, 'fav_books_app/index.html')

def success(request):
    if "first_name" in request.session:
        context = {
            'books': Book.objects.all(),
        }
        return render(request, "fav_books_app/success.html", context)
    return redirect('/')


def one_book(request, book_id):
    book = Book.objects.get(id=book_id)
    this_book_fans = book.fans.all()
    context ={
        "book": book,
        "this_book_fans": this_book_fans,
    }
    return render(request, "fav_books_app/book.html", context)

def add_book(request):
    if request.method == "GET":
        return redirect("/")
    if request.method == "POST":# pass the post data to the method we wrote and save the response in a variable called errors
        errors = Book.objects.basic_validator(request.POST)
        if len(errors) > 0:
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect('/')
        title = request.POST["book_title"]
        description = request.POST["book_description"]
        new_book = Book.objects.create(title=title, description=description)
        new_book.fans.add(User.objects.get(id=request.session['id']))
        print(new_book.title)
        return redirect("/success")


def login(request):
    errors = {}
    if request.method == "POST":
        possible_user = User.objects.filter(email=request.POST["email"])
        try:
            this_user = possible_user[0]
            if request.POST["password"] == this_user.password:
                request.session['first_name'] = this_user.first_name
                request.session['id'] = this_user.id
                request.session['last_name'] = this_user.last_name
                return redirect("/success")
            errors['password_oopsie_error']= "You seem to have forgotten your password. Too bad for you, we for sure don't save your plaintext password so get a new email and come back."
        except:
            errors['email_oopsie_error']=  "No user exists with this email, go ahead and register!"
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
    return redirect("/")

def reg(request):
    if request.method == "POST":
        # pass the post data to the method we wrote and save the response in a variable called errors
        errors = User.objects.basic_validator(request.POST) 
        if request.POST["password"] != request.POST["confirm_password"]:
            errors['pw_confrimation_fail'] = "Password does not match confirmation password"     
        # check if the errors dictionary has anything in it
        if len(errors) > 0:
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect('/')
        else:
            password = request.POST["confirm_password"]
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            email = request.POST["email"]
            new_user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
            request.session['first_name'] = new_user.first_name
            request.session['last_name'] = new_user.last_name
            request.session['id'] = new_user.id
    return redirect("/success")

# def success(request):
#     if "first_name" in request.session:
#         return render(request, "fav_books_app/success.html")
#     return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')