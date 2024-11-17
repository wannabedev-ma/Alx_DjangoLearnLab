# relationship_app/urls.py

from django.urls import path
from .views import list_books, LibraryDetailView, register, CustomLoginView, CustomLogoutView

urlpatterns = [

    path('book/', views.list_books, name='book_list'),
    path('add_book/', views.add_book, name='add_book'),  
    path('edit_book/', views.edit_book, name='edit_book'),  
    path('book/<int:pk>/delete/', views.delete_book, name='delete_book'),

    
    path('books/', list_books, name='list_books'),  # URL for listing books in plain text
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL for library detail view
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('register/', views.register, name='register'),
]
