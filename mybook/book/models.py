from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.urls import reverse


class Book(models.Model):
    NOT_READ = '1'
    READING = '2'
    READ = '3'

    READ_STATUS = (
        (NOT_READ, '읽지않음'),
        (READING, '읽는중'),
        (READ, '읽음'),
    )

    title = models.CharField(verbose_name='타이틀', max_length=100)
    contents = models.CharField(verbose_name='서평', max_length=300, null=True, blank=True)
    read_status = models.CharField(verbose_name='책 상태', max_length=1, choices=READ_STATUS,
                                   default=NOT_READ, blank=False)
    purchase_date = models.DateField(verbose_name='구매일', null=True)
    created = models.DateTimeField(verbose_name='등록일', auto_now_add=True)
    user = models.ForeignKey('User', verbose_name='사용자',
                             on_delete=models.CASCADE,
                             null=False, blank=False)

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})

    @property
    def read_status_class(self):
        if self.read_status is self.NOT_READ:
            return "badge-default"
        elif self.read_status is self.READING:
            return "badge-info"
        else:
            return "badge-primary"

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
    email = models.EmailField(unique=True, verbose_name='Email')
    name = models.CharField(max_length=20, verbose_name='이름')
    nick_name = models.CharField(max_length=20, verbose_name='닉네임', blank=True)
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

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

        def __str__(self):
            return self.name
