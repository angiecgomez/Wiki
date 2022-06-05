from django.http.request import validate_host
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entry_page, name="entry_page"),
    path("error_page", views.error_page, name="error_page"),
    path("search", views.search_encyclopedia, name="search_encyclopedia"),
    path("create_page", views.create_page, name="create_page"),
    path("save_newpage", views.save_newpage, name="save_newpage"),
    path("edit_page/<str:entry>", views.edit_page, name="edit_page"),
    path("update_page", views.update_page, name="update_page"),
    path("random_page", views.random_page, name="random_page")
]
