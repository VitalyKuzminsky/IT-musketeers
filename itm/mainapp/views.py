from audioop import reverse
from datetime import datetime as dt
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.views.generic import TemplateView, DetailView

from mainapp.data_library import get_orders_filter
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
    model = Category
    extra_context = {'title': 'Web-Разработка'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Services.objects.filter(category_id=Category.objects.filter(name='Web-Разработка')[0])
        context['category'] = Category.objects.filter(name='Web-Разработка')
        return context

    template_name = 'mainapp/web.html'


class MobilPageView(TemplateView):
    model = Category
    extra_context = {'title': 'Мобильная Разработка'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Services.objects.filter(category_id=Category.objects.filter(name='Мобильная Разработка')[0])
        context['category'] = Category.objects.filter(name='Мобильная Разработка')
        return context
    template_name = 'mainapp/mobile.html'


class MarketingPageView(TemplateView):
    model = Category
    extra_context = {'title': 'Маркетинг'}

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
        context_data['reviews'] = Reviews.objects.filter(services_id=self.kwargs.get('pk'))
        return context_data

    def post(self, request, *args, **kwargs):
        if request.POST.get('type') == 'make_order':
            new_order = Basket
            new_order.objects.create(
                custom_user_id=CustomUser.objects.filter(pk=request.user.id)[0],
                service_id=Services.objects.filter(pk=self.kwargs.get('pk'))[0]
            )
            return JsonResponse({'status': 'OK'})


class ReviewPageView(TemplateView):
    template_name = 'mainapp/review.html'
    extra_context = {'title': 'Оставить отзыв'}
    model = Reviews

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['service'] = get_object_or_404(Services, pk=self.kwargs.get('pk'))
        return context_data

    def post(self, request, *args, **kwargs):
        if all((request.POST.get('rating'), request.POST.get('text_content'))):
            new_review = Reviews
            data_add = {
                'custom_user_id': CustomUser.objects.filter(pk=request.user.id)[0],
                'services_id': Services.objects.filter(pk=self.kwargs.get('pk'))[0],
                'content': request.POST.get('text_content'),
                'estimation': request.POST.get('rating')
            }
            new_review.objects.create(**data_add)

            return redirect('service_detail', pk=self.kwargs.get('pk'))
        else:
            context_data = super().get_context_data(**kwargs)
            context_data['service'] = get_object_or_404(Services, pk=self.kwargs.get('pk'))
            context_data['message_err'] = 'Заполните все поля'

            return redirect('review', pk=self.kwargs.get('pk'))


class ContactsPageView(TemplateView):
    template_name = 'mainapp/contacts.html'


class OrderPageView(TemplateView):
    template_name = 'mainapp/order.html'
    extra_context = {'title': 'Заказы'}
    model = Basket

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['orders'] = Basket.objects.all()
        context_data['statuses'] = {
            'COMPLETED': 'Завершен',
            'IN_PROCCESS': 'В разработке',
            'DID_NOT_START': 'Не приступалось'
        }
        context_data['authors'] = CustomUser.objects.filter(is_superuser=True)
        context_data['clients'] = CustomUser.objects.filter(is_superuser=False)
        return context_data

    def post(self, request, *args, **kwargs):
        if request.POST.get('type') == 'status_service':
            new_status = request.POST.get('status')
            basket = Basket.objects.filter(pk=request.POST.get('order_id'))
            basket.update(status_completed=new_status)
            return JsonResponse({'status': 'OK'})

        if request.POST.get('type') == 'filter_result':
            skip_list = ['csrfmiddlewaretoken', 'type']
            filter_dict = {key: val for key, val in request.POST.items() if key not in skip_list and val}

            result_dict = get_orders_filter(filter_data=filter_dict)
            result_js = []
            if result_dict:
                for order in result_dict:
                    result_js.append({
                        'id': order[0],
                        'author': order[1],
                        'custom_user_id': order[2],
                        'service_id': order[3],
                        'create_date': order[4],
                        'pay_date': order[5],
                        'status_completed': order[6]
                    })
            return JsonResponse({'res': result_js})


class MobilDetailPageView(TemplateView):
    template_name = 'mainapp/mobile_detail.html'


class MarketingDetailPageView(TemplateView):
    template_name = 'mainapp/marketing_detail.html'


# class DesignPageView(TemplateView):
#     template_name = 'mainapp/design.html'