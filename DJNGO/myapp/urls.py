from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookView.as_view(), name="index_book"),
    path('listasa/', views.BookList.as_view(), name="booklist"),
]