from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django import forms
from django.contrib.auth import get_user_model


class LoginUserForm(AuthenticationForm):

    username = forms.CharField(label='Логин', widget=forms.TextInput(
                attrs={
                    'class': 'form-control mb-4',
                    'placeholder': 'Введите свой логин'
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
                # Поле не обязательно
                required=False
                )
    
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(
                attrs={
                    'class': 'form-control mb-4',
                    'placeholder': 'Введите свою Фамилию'
                }),
                # Поле не обязательно
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
                # Поле не обязательно
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
    
    # Очерёдность полей формы
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

    class Meta:
        model = get_user_model()
        fields = [
            'username',
        ]
        field_classes = {'username': UsernameField}

    