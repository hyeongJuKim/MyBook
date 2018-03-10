from django.contrib import admin
from .models import Book, User


class BookAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Book._meta.fields]
    search_fields = ('title',)


admin.site.register(Book, BookAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = [f.name for f in User._meta.fields]
    search_fields = ('name',)


admin.site.register(User, UserAdmin)
