# library/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('books/', views.book_list, name='book_list'),
    path('books/add/', views.book_create, name='book_add'),
    path('books/<int:pk>/edit/', views.book_update, name='book_edit'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('members/', views.member_list, name='member_list'),
    path('members/add/', views.member_create, name='member_add'),
    path('members/<int:pk>/edit/', views.member_update, name='member_edit'),
    path('members/<int:pk>/delete/', views.member_delete, name='member_delete'),
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('transactions/add/', views.transaction_create, name='transaction_add'),
    path('transactions/<int:pk>/return/', views.return_book, name='return_book'),
    path('search/', views.search_books, name='search_books'),
]