from django.contrib.auth.views import LoginView, LogoutView
from django.http import JsonResponse
from django.views.generic import TemplateView, CreateView
from authapp.forms import LoginUserForm, CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.utils import dateformat
from authapp.models import CustomUser
from mainapp.models import Basket
from datetime import datetime as dt


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


class ProfilePageView(LoginRequiredMixin, TemplateView):
    template_name = 'mainapp/profile.html'

    def get_queryset(self):
        some_param = self.request.user.pk  # Здесь может быть ваш параметр
        return Basket.objects.filter(custom_user_id=some_param)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filtered_objects'] = self.get_queryset()
        context['user_name'] = self.request.user.username
        return context

    def post(self, request, *args, **kwargs):
        if request.POST.get('type') == 'pay_order':
            order = Basket.objects.filter(pk=request.POST.get('order_id'))
            order.update(
                pay_date=dt.now()
            )
            return JsonResponse({'status': 'OK'})
