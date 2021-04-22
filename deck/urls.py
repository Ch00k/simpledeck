from django.urls import path

from . import views

urlpatterns = [
    path("", views.DeckListView.as_view(), name="list"),
    path("create/", views.show_create_update, name="create"),
    path("<int:pk>/", views.show_create_update, name="show"),
    path("preview/<int:pk>", views.present, name="preview"),
    path("delete/<int:pk>", views.delete, name="delete"),
]
