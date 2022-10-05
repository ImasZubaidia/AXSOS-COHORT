from multiprocessing import context
from turtle import title
from django.shortcuts import redirect, render
from .models import Show

def add_new_show_page(request):
    return render (request,  "add_show.html")


def create_show(request):
    post = request.post

    created_show = Show.objects.create(
        title=post["title"],
        network=post["network"],
        release_date=post["release_date"],
        description=post["description"],
        )

    return redirect(f"/shows/{created_show.id}")


# def show_details(request, show_id):
#         context = {
#             "individual_show": Show.objects.get(id=show_id)
#         }

#         return render(request,"show_details.html" , context)

# def delete_show(request, show_id):
#         show_to_delete = Show.objects.get
#         id=show_id
#         show_to_delete.delete()

# def all_shows(request):
#             context = {
#                 "shows":show.objects.all()
#             }
#             return render(request, "all_shows.html",context)

# def edit_show(request, show_id):
#     context = {
#         "show": Show.objects.get(id=show_id)
#     }

#     return render( request , "edit_show", context)