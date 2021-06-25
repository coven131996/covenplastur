from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic


# Create your views here.
def index(request):
    # Genera contadores de algunos de los objetos principales
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    
    num_authors=Author.objects.all().count()  # El 'all()' esta implícito por defecto.
    num_instances=Author.objects.all().count()
    num_instances_available=Author.objects.all().count()
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},        
                  )
class BookListView(generic.ListView):
    model = Book
    paginate_by = 6    
    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context
    template_name = 'books/my_arbitrary_template_name_list.html'    
  
  
      
class BookDetailView(generic.DetailView):
    model = Book 
    context_object_name = 'my_book_list'  
    queryset = Book.objects.filter()
    def get_queryset(self):
        return Book.objects.filter(title__icontains='war')
    
 #Vista para el author   
    
class AuthorListView(generic.ListView):
    model = Author  
    def get_context_data(self, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context
    
class AutorDetailView(generic.DetailView):
    model = Author  
    def get_queryset(self):
        return Author.objects.filter(first_name__last_name='war')[:5] 

