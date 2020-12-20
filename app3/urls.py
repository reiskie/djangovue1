from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    url(r'add_book$', views.add_book, ),
    url(r'show_books$', views.show_books, ),
    url(r'^list$', views.list, name = 'list-url'),
    url(r'^test$', views.test), 
]

