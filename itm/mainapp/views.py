from django.shortcuts import get_object_or_404
from django.views import generic
from django.views.generic import TemplateView, DetailView
from mainapp.models import *


class MainPageView(generic.ListView):
    extra_context = {'title': 'Главная страница'}
    model = Category

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['category'] = Category.objects.all()
        context['our_works'] = WorkExample.objects.filter(deleted=False)
        return context

    template_name = 'mainapp/main.html'


class WebPageView(TemplateView):
    model = Category.objects.filter(name='Web-Разработка')
    extra_context = {'title': model[0]}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Services.objects.filter(category_id=Category.objects.filter(name='Web-Разработка')[0])
        context['category'] = Category.objects.filter(name='Web-Разработка')
        return context

    template_name = 'mainapp/web.html'


class MobilPageView(TemplateView):
    model = Category.objects.filter(name='Мобильная Разработка')
    extra_context = {'title': model[0]}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Services.objects.filter(category_id=Category.objects.filter(name='Мобильная Разработка')[0])
        context['category'] = Category.objects.filter(name='Мобильная Разработка')
        return context
    template_name = 'mainapp/mobile.html'


class MarketingPageView(TemplateView):
    model = Category.objects.filter(name='Маркетинг')
    extra_context = {'title': model[0]}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Services.objects.filter(category_id=Category.objects.filter(name='Маркетинг')[0])
        context['category'] = Category.objects.filter(name='Маркетинг')
        return context
    template_name = 'mainapp/marketing.html'


class ServiceDetailPageView(DetailView):
    template_name = 'mainapp/detail.html'
    model = Services

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['service'] = get_object_or_404(Services, pk=self.kwargs.get('pk'))
        return context_data


class ContactsPageView(TemplateView):
    template_name = 'mainapp/contacts.html'


class OrderPageView(TemplateView):
    template_name = 'mainapp/order.html'


class ReviewPageView(TemplateView):
    template_name = 'mainapp/review.html'


class MobilDetailPageView(TemplateView):
    template_name = 'mainapp/mobile_detail.html'


class MarketingDetailPageView(TemplateView):
    template_name = 'mainapp/marketing_detail.html'


# class DesignPageView(TemplateView):
#     template_name = 'mainapp/design.html'