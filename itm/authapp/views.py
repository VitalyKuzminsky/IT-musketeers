from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from authapp.forms import LoginUserForm


class RegPageView(TemplateView):
    template_name = 'mainapp/register.html'


class AuthPageView(LoginView):
    template_name = 'mainapp/auth.html'
    form_class = LoginUserForm


class CustomLogoutView(LogoutView):
    pass


class ProfilePageView(TemplateView):
    template_name = 'mainapp/profile.html'

