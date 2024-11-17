from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

def retrieve_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian

# Example usage (uncomment to test):
# author = query_books_by_author("John Doe")
# library_books = list_books_in_library("Main Library")
# librarian = retrieve_librarian_for_library("Main Library")
# print(author)  # Output: Book objects associated with John Doe
# print(library_books)  # Output: Book objects in the Main Library
# print(librarian)  # Output: Librarian object for the Main Library