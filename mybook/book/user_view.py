from django.views.generic import FormView, DetailView, TemplateView
from django.contrib.auth.views import LoginView
from .models import User
from .forms import UserCreationForm, UserLoginForm
from django.urls import reverse


class UserCV(FormView):
    form_class = UserCreationForm
    fields = ['email', 'name', 'nick_name']
    template_name = 'book/user_create.html'

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('login')


class UserDV(DetailView):
    model = User
    template_name = 'book/user_detail.html'
    context_object_name = 'user'


class MyPageView(TemplateView):
    model = User
    template_name = 'book/user_detail.html'

    def get_context_data(self, **kwargs):
        print(self.request.user)
        return {'user' : self.request.user}



class UserLoginView(LoginView):
    authentication_form = UserLoginForm
    template_name = 'book/user_login.html'
    context_object_name = 'user'

    def get_success_url(self):
        return reverse('mypage')
