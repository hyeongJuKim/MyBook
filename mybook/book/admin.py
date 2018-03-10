from django.contrib import admin
from .models import Book, User
from django import forms
from django.contrib.auth.models import Group


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='password_confirm', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'nick_name')

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("password dont match")

        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'nick_name')

    def clean_password(self):
        return self.cleaned_data['password']


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
