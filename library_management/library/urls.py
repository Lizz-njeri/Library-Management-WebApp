from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.manage_books, name='manage_books'),
    path('members/', views.manage_members, name='manage_members'),
    path('transactions/', views.manage_transactions, name='manage_transactions'),
    path('search/', views.search_books, name='search_books'),
]
