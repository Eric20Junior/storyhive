from django.urls import path
from .views import BookListView, BookDetailView,BookCreateView, BookUpdateView, BookDeleteView, CommentList, CommentDetail
from . import views

urlpatterns = [
   path('', views.apiOverView, name='apiOverView'),
   path('books/', BookListView.as_view(), name='books'), 
   path('book-detail/<int:pk>/', BookDetailView.as_view(), name='book-detail'), 
   path('create-book/', BookCreateView.as_view(), name='create-book'),
   path('update-book/<int:pk>/', BookUpdateView.as_view(), name='update-book'), 
   path('delete-book/<int:pk>/', BookDeleteView.as_view(), name='delete-book'),


    path('comments/', CommentList.as_view(), name='comments'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
]
