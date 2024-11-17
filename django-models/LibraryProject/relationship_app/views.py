from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Library, Books 
from django.contrib.auth.decorators import permission_required, login_required, user_passes_test
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
    if form.is_valid():
            form.save()  # Save the new user
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html',)
def home(request):
    return render(request, 'relationship_app/home.html')
# Function-based view to list all books using a template
def list_books(request):
    # Retrieve all books
    books = Book.objects.all()
    context= {'book_list':books}
    return render(request,'relationship_app/list_books.html', context )
    # Render the list using a template
    
# Class-based view to display details of a specific library, listing all books in that library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
# View for adding a new book

@permission_required('relationship_app.can_add_book', raise_exception=True)

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
    if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form})


@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/book_form.html', {'form': form})

# View for deleting a book
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})