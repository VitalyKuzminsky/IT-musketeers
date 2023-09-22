from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, CreateView
from authapp.forms import LoginUserForm, CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model


class RegPageView(CreateView):
    model = get_user_model()
    template_name = 'mainapp/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('auth')


class AuthPageView(LoginView):
    template_name = 'mainapp/auth.html'
    form_class = LoginUserForm


class CustomLogoutView(LogoutView):
    pass


class ProfilePageView(TemplateView):
    template_name = 'mainapp/profile.html'

