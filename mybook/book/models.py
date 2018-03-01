from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


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


class User(AbstractBaseUser):
    name = models.CharField(max_length=20)
    nick_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    USERNAME_FIELD = 'name'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

        def __str__(self):
            return self.name
