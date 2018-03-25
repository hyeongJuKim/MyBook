from .models import User, Book
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='비밀번호 재입력', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'name')
        labels = {
            'email': 'Email',
            'name': '이름',
        }

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("입력하신 비밀번호가 일치 하지 않습니다.")

        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

        return user


class UserChangeForm(forms.ModelForm):
    current_password = forms.CharField(label='비밀번호', widget=forms.PasswordInput, required=False)
    password = forms.CharField(label='변경 비밀번호', widget=forms.PasswordInput, required=False)
    password_confirm = forms.CharField(label='변경 비밀번호 확인', widget=forms.PasswordInput, required=False)


    class Meta:
        model = User
        fields = ('email', 'nick_name', 'name')

    def clean_current_password(self):
        current_password = self.data['current_password']

        if not current_password:
            return current_password


        email = self.cleaned_data['email']
        user = self._meta.model.objects.get(email=email)

        if not user.check_password(current_password):
            raise forms.ValidationError("현재 비밀번호가 일치 하지 않습니다.")


    def clean_password(self):
        current_password = self.data['current_password']
        password = self.cleaned_data['password']

        if not current_password:
            return None
        else:
            if not password:
                raise forms.ValidationError("변경할 비밀번호를 입력해주세요")

        return self.cleaned_data['password']


    def clean_password_confirm(self):
        current_password = self.data['current_password']
        password = self.data['password']
        password_confirm = self.cleaned_data['password_confirm']

        if not current_password:
            return None
        else:
            if password and password_confirm and password != password_confirm:
                raise forms.ValidationError("입력하신 비밀번호가 일치 하지 않습니다.")

        return self.cleaned_data['password_confirm']


    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data['password']

        if password is not None:
            print(user.name)
            user.set_password(password)

        if commit:
            user.save()
            return user


class UserLoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pass


class BookForm(forms.ModelForm):
    contents = forms.CharField(label='서평', required=False,
                               widget=forms.Textarea(
                                   attrs={'rows': 5, 'cols': 100}))
    purchase_date = forms.DateField(label='구매일', required=False,
                                    widget=forms.DateInput(
                                        attrs={'type': 'date'}))

    class Meta:
        model = Book
        fields = ['title', 'contents', 'user', 'purchase_date', 'read_status']

