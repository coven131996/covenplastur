from django.db import models
from django.db.models import fields
from django.urls import reverse
import uuid 
from django.contrib import admin
# Create your models here.

class Genre(models.Model):
     name = models.CharField(max_length=200, help_text="Ingrese el nombre del género (p. ej. Ciencia Ficción, Poesía Francesa etc.)")

     def __str__(self):
        return self.name

class MyModelName(models.Model):
    
    my_field_name = models.CharField(max_length=20, help_text="Enter field documentation")
    
class Meta:
    ordering = ["-my_field_name"]
    ordering = ["title", "-pubdate"]
    verbose_name = "BetterName"
    
    def __str__(self):
        return self.field_name
    
    def get_absolute_url(self):   
        return reverse('model-detail-view', args=[str(self.id)]) 
    
class Book(models.Model): 
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Ingrese una breve descripción del libro")
    isbn = models.CharField('ISBN',max_length=13, help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text="Seleccione un genero para este libro")
   
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)]) 
    
class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para este libro particular en toda la biblioteca")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),)

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Disponibilidad del libro')

class Meta:
        ordering = ["due_back"]

def __str__(self):
        
        return '%s (%s)' % (self.id,self.book.title) 
  
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
    
    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)
    class Meta:
        ordering = ['last_name']

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]    
     
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    fields = ['title', 'author', 'display_genre']
     
    def display_genre(self):
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    display_genre.short_description = 'Genre'
     
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')          