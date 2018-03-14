from django.views.generic import CreateView, FormView, DetailView
from .models import User
from .forms import UserCreationForm

class UserCV(FormView):
    form_class = UserCreationForm
    fields = ['email', 'name', 'nick_name']
    template_name = 'book/user_create.html'

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        url = self.object.get_absolute_url()
        return url

class UserDV(DetailView):
    model = User
    template_name = 'book/user_detail.html'
    context_object_name = 'user'










