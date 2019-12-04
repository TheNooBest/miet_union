from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Такого пользователя нет')
            if not user.check_password(password):
                raise forms.ValidationError('Неверный пароль')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class StudentMoneyForm(forms.Form):
    ФИО = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    Группа = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    Адрес_проживания = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    Причина = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    Дата = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    year = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    Серия_Паспорта = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    Номер_Паспорта = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    Дата_Выдачи = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    Место_Выдачи = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    Телефон = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean(self, *args, **kwargs):
        ФИО = self.cleaned_data.get('ФИО')
        Группа = self.cleaned_data.get('Группа')
        Адрес_проживания = self.cleaned_data.get('Адрес_проживания')
        Причина = self.cleaned_data.get('Причина')
        Дата = self.cleaned_data.get('Дата')
        Год = self.cleaned_data.get('Год')
        Серия_Паспорта = self.cleaned_data.get('Серия_Паспорта')
        Номер_Паспорта = self.cleaned_data.get('Номер_Паспорта')
        Дата_Выдачи = self.cleaned_data.get('Дата_Выдачи')
        Место_Выдачи = self.cleaned_data.get('Место_Выдачи')
        Телефон = self.cleaned_data.get('Телефон')

        # if username and password:
        #     user = authenticate(username=username, password=password)
        #     if not user:
        #         raise forms.ValidationError('Такого пользователя нет')
        #     if not user.check_password(password):
        #         raise forms.ValidationError('Неверный пароль')
        return super(StudentMoneyForm, self).clean(*args, **kwargs)