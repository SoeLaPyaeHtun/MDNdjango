from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookInstance, Language

class AuthorAdmin(admin.ModelAdmin):
    pass

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


    

#admin.site.register(Book)
admin.site.register(Language)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Genre)
#admin.site.register(BookInstance)
