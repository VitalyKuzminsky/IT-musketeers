from django.views import generic
from django.views.generic import TemplateView
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
    template_name = 'mainapp/web.html'


class WebDetailPageView(TemplateView):
    template_name = 'mainapp/web_detail.html'


class MobilPageView(TemplateView):
    template_name = 'mainapp/mobile.html'


class MobilDetailPageView(TemplateView):
    template_name = 'mainapp/mobile_detail.html'


class MarketingPageView(TemplateView):
    template_name = 'mainapp/marketing.html'


class MarketingDetailPageView(TemplateView):
    template_name = 'mainapp/marketing_detail.html'


class ContactsPageView(TemplateView):
    template_name = 'mainapp/contacts.html'


class OrderPageView(TemplateView):
    template_name = 'mainapp/order.html'


class ReviewPageView(TemplateView):
    template_name = 'mainapp/review.html'


# class DesignPageView(TemplateView):
#     template_name = 'mainapp/design.html'