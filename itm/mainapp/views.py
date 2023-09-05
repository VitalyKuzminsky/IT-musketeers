from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = 'mainapp/main.html'


class WebPageView(TemplateView):
    template_name = 'mainapp/web.html'


class MobilPageView(TemplateView):
    template_name = 'mainapp/mobile.html'


class MarketingPageView(TemplateView):
    template_name = 'mainapp/marketing.html'


class DesignPageView(TemplateView):
    template_name = 'mainapp/design.html'


class ContactsPageView(TemplateView):
    template_name = 'mainapp/contacts.html'