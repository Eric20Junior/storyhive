from django.urls import path
from . import views

urlpatterns = [
   path('', views.apiOverView, name='apiOverView'),
   path('books/', views.BookListView, name='books'), 
   path('book-detail/<int:pk>/', views.BookDetailView, name='book-detail'), 
   path('create-book/', views.BookCreateView, name='create-book'),
   path('update-book/<int:pk>/', views.BookUpdateView, name='update-book'), 
   path('delete-book/<int:pk>/', views.BookDeleteView, name='delete-book'), 

]
