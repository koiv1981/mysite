from django import forms
from .models import News

from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={"class": "form-control", "autocomplete": "off"}))
    email = forms.EmailField(label="Адрес электронной почты", widget=forms.EmailInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={"class": "form-control", "autocomplete": "off"}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-control", }))


class ContactForm(forms.Form):
    subject = forms.CharField(label="Тема",
                               widget=forms.TextInput(attrs={"class": "form-control", "autocomplete": "off"}))
    content = forms.CharField(label="Текст",
                              widget=forms.Textarea(attrs={"class": "form-control", "autocomplete": "off", "rows": 5}))


class NewsForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        #fields = "__all__"
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            'category': forms.Select(attrs={"class": "form-control"}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        lis = "1234567890"
        if title[0] in lis:
            raise ValidationError("Название новости не должно начинаться с цифры")
        return title
