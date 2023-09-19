from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, CreateView
from authapp.forms import LoginUserForm, CustomUserCreationForm
from django.urls import reverse_lazy
from authapp import models
from django.http.response import HttpResponseRedirect
from django.contrib.auth import password_validation


class RegPageView(CreateView):
    template_name = 'mainapp/register.html'
    form_class = CustomUserCreationForm

    def post(self, request, *args, **kwargs):
        try:
            if all(
                (
                    request.POST.get("username"),
                    request.POST.get("email"),
                    request.POST.get("password1"),
                    password_validation.validate_password(request.POST.get("password1")) == None,
                    request.POST.get("password1") == request.POST.get("password2"),
                )
            ):
                new_user = models.CustomUser.objects.create(
                    username=request.POST.get("username"),
                    first_name=request.POST.get("first_name"),
                    last_name=request.POST.get("last_name"),
                    birthday=request.POST.get("birthday"),
                    email=request.POST.get("email"),
                    phone=request.POST.get("phone"),
                )
                new_user.set_password(request.POST.get("password1"))
                new_user.save()
                return HttpResponseRedirect(reverse_lazy("auth"))
        except Exception as exp:
            return HttpResponseRedirect(reverse_lazy("registration"))


class AuthPageView(LoginView):
    template_name = 'mainapp/auth.html'
    form_class = LoginUserForm


class CustomLogoutView(LogoutView):
    pass


class ProfilePageView(TemplateView):
    template_name = 'mainapp/profile.html'

