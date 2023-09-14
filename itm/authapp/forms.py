from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from authapp.models import CustomUser


class LoginUserForm(AuthenticationForm):

    username = forms.CharField(label='Логин', widget=forms.TextInput(
                attrs={
                    'class': 'form-control mb-4',
                    'placeholder': 'Введите свой Email'
                }))

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
                attrs={
                    'class': 'form-control mb-4',
                    'placeholder': 'Введите пароль'
                }))
    
    

class CustomUserCreationForm(UserCreationForm):

    username = forms.CharField(label='Логин*', widget=forms.TextInput(
                attrs={
                    'class': 'form-control mb-4',
                    'placeholder': 'Введите свой Логин'
                }))
    
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(
                attrs={
                    'class': 'form-control mb-4',
                    'placeholder': 'Введите своё Имя'
                }),
                required=False
                )
    
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(
                attrs={
                    'class': 'form-control mb-4',
                    'placeholder': 'Введите свою Фамилию'
                }),
                required=False
                )
    
    birthday = forms.CharField(label='День рождения*', widget=forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control mb-4',
                    'placeholder': 'Введите День рождения',
                }))
    
    email = forms.CharField(label='Email*', widget=forms.TextInput(
                attrs={
                    'class': 'form-control mb-4',
                    'placeholder': 'Укажите Электронную почту',
                }))
    
    phone = forms.CharField(label='Телефон', widget=forms.TextInput(
                attrs={
                    'class': 'form-control mb-4',
                    'placeholder': '+7(999)999-99-99',
                }),
                required=False
                )
    
    password1 = forms.CharField(label='Пароль*', widget=forms.PasswordInput(
                attrs={
                    'class': 'form-control mb-4',
                    'placeholder': 'Введите пароль'
                }))
    
    password2 = forms.CharField(label='Повторите пароль*', widget=forms.PasswordInput(
                attrs={
                    'class': 'form-control mb-4',
                    'placeholder': 'Повторите пароль'
                }))
    
    submit = forms.CharField(label='', widget=forms.TextInput(
                attrs={
                    'type': 'submit',
                    'class': 'form-control mb-4 w-50 mx-auto',
                    'value': 'Зарегистрироваться'
                }))
    

    field_order = [
        'username', 
        'first_name', 
        'last_name', 
        'phone', 
        'birthday', 
        'email',  
        'password1', 
        'password2', 
        'submit'
        ]
    