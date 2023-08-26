from django.urls import path

from . import views

app_name = "apis"
urlpatterns = [path("book_list/", views.BookListApi.as_view(), name="book_list")]
