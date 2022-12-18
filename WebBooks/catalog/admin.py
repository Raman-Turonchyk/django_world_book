from django.contrib import admin
from .models import Author, Book, Gener, Language, Status, BookInstance


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'day_of_birth', 'day_of_death')
    fields = ['first_name', 'last_name', ('day_of_birth', 'day_of_death')]


class BookInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    list_filter = ('genre', 'author')
    inlines = [BookInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('book', 'status')
    fieldsets = (
        ('Экземляр книги', {
            'fields': ('book', 'imprint', 'inv_nom')
        }),
        ('Статус и окончание его действия', {
            'fields': ('status', 'due_back', 'borrower')
        })
    )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Gener)
admin.site.register(Language)
admin.site.register(Status)
# admin.site.register(Book)
# admin.site.register(BookInstance)



