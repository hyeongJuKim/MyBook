from django.contrib import admin
from .models import Book, User
from django.contrib.auth.models import Group
from .forms import UserChangeForm, UserCreationForm


class BookAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Book._meta.fields]
    search_fields = ('title',)


class UserAdmin(admin.ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'name', 'is_admin')
    search_fields = ('name',)


admin.site.register(Book, BookAdmin)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
