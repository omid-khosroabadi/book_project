from django.contrib import admin
from .models import Books, Comment


class CommentSub(admin.TabularInline):
    model = Comment
    fields = ['author', 'body', 'star', 'recommend']
    extra = 1


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    inlines = [
        CommentSub,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'star']


