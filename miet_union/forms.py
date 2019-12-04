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
    fio = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    group = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    addr = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    reason = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    daymonth = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    year = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    ser = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    num = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    pas_date = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    pas_place = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self, *args, **kwargs):
        fio = self.cleaned_data.get('fio')
        group = self.cleaned_data.get('group')
        addr = self.cleaned_data.get('addr')
        reason = self.cleaned_data.get('reason')
        daymonth = self.cleaned_data.get('daymonth')
        year = self.cleaned_data.get('year')
        ser = self.cleaned_data.get('ser')
        num = self.cleaned_data.get('num')
        pas_date = self.cleaned_data.get('pas_date')
        pas_place = self.cleaned_data.get('pas_place')
        phone = self.cleaned_data.get('phone')

        # if username and password:
        #     user = authenticate(username=username, password=password)
        #     if not user:
        #         raise forms.ValidationError('Такого пользователя нет')
        #     if not user.check_password(password):
        #         raise forms.ValidationError('Неверный пароль')
        return super(StudentMoneyForm, self).clean(*args, **kwargs)