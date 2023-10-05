from django.views.generic import TemplateView
from mainapp.models import *


class MainPageView(TemplateView):
    template_name = 'mainapp/main.html'


class WebPageView(TemplateView):
    template_name = 'mainapp/web.html'
    # web_services = Services.objects.filter(category_id=2)
    # extra_context = web_services
    # print(Category.objects.filter(name='Web-разработка'))


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


# class DesignPageView(TemplateView):
#     template_name = 'mainapp/design.html'