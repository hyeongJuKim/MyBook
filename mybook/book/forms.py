from .models import User
from django import forms


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='비밀번호 재입력', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'name')
        labels = {
            'email' : 'Email',
            'name' : '이름',
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
    class Meta:
        model = User
        fields = ('email', 'nick_name')

    def clean_password(self):
        return self.cleaned_data['password']
