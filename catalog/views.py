from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre

# Create your views here.


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    num_genres_fantasy = Genre.objects.filter(name__contains='Fantasy').count()

    num_books_hunger = Book.objects.filter(title__contains='Hunger').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres_fantasy': num_genres_fantasy,
        'num_books_hunger': num_books_hunger,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
