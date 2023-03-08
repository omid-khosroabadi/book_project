from django.urls import path
from . import views


urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book_detail/<int:pk>/', views.book_detail, name='book_detail'),
    path('comment_create/<int:pk>/', views.CommentCreate.as_view(), name='comment_create'),
    path('comment_delete/<int:pk>/', views.CommentDelete.as_view(), name='comment_delete'),
    path('comment_update/<int:pk>/', views.CommentUpdate.as_view(), name='comment_update'),
    path('book_add/', views.book_add, name='book_add'),
    path('book_delete/<int:pk>/', views.BookDelete.as_view(), name='book_delete'),
    path('book_update/<int:pk>/', views.BookUpdate.as_view(), name='book_update'),
]
