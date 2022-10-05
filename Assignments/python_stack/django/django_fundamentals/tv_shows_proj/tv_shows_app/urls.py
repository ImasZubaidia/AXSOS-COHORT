from django.urls import path 
from . import views

urlpatterns = [
    path('shows/new', views.add_new_show_page ),
    path("shows/create",views.create_show),
    ]
#     path('shows/<int : show_id>',views.show_details),
#     path("shows/<int:show_id>/delete", views.delete_show),
#     path("shows", views.all_shows),
#     # path ("shows/<int:show_id>/edit",views.edit_show),
# ]