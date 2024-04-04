from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new", views.new, name="new"),
    path("create", views.create, name="create"),
    path("<id>/edit", views.edit, name="edit"),
    path("update/<id>", views.update, name="update"),
    path("delete/<id>", views.delete, name="delete"),
    path("<id>", views.show, name='show'),
]