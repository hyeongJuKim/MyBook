from django.views.generic import FormView, DetailView, TemplateView, UpdateView, CreateView
from django.contrib.auth.views import LoginView
from .models import User
from .forms import *
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash

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


class MyPageView(UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = 'book/user_update.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        form = self.get_form()
        if form.is_valid():
            # 비밀번호 변경으로 세션 초기화되 다시 세션 값을 설정 해줌
            response = self.form_valid(form)
            user = self.object
            update_session_auth_hash(request, user)

            return response
        else:
            return self.form_invalid(form)


    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('mypage')


class UserLoginView(LoginView):
    authentication_form = UserLoginForm
    template_name = 'book/user_login.html'
    context_object_name = 'user'

    def get_success_url(self):
        return reverse('mypage')
