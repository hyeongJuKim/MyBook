from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import BaseUserManager

class Book(models.Model):
    title = models.CharField(max_length=100)
    contents = models.CharField(max_length=300, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('User',
                             on_delete=models.CASCADE,
                             null=False, blank=False)

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'

        def __str__(self):
            return self.title

class UserManager(BaseUserManager):
    def create_user(self, email, name, nick_name=None, password=None):
        if not email:
            raise ValueError("User must have an email")

        user = self.model(email=email, name=name, nick_name=nick_name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, name, password):
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.is_admin = True
        user.save()


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=20)
    nick_name = models.CharField(max_length=20)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

        def __str__(self):
            return self.name
