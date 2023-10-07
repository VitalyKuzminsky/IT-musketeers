from django.urls import path
from mainapp.views import *
from authapp.views import *


urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),

    path('registration/', RegPageView.as_view(), name='registration'),
    path('auth/', AuthPageView.as_view(), name='auth'),
    path('profile/', ProfilePageView.as_view(), name='profile'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    path('web-development/', WebPageView.as_view(), name='web'),
    path('web-development/<int:pk>/detail', WebDetailPageView.as_view(), name='web_detail'),
    path('mobile-development/', MobilPageView.as_view(), name='mobile'),
    path('mobile-development/<int:pk>/detail', MobilDetailPageView.as_view(), name='mobile_detail'),
    path('marketing/', MarketingPageView.as_view(), name='marketing'),
    path('marketing/<int:pk>/detail', MarketingDetailPageView.as_view(), name='marketing_detail'),
    path('order/', OrderPageView.as_view(), name='order'),
    path('review/', ReviewPageView.as_view(), name='review'),

    # path('design/', DesignPageView.as_view(), name='design'),

    path('contacts/', ContactsPageView.as_view(), name='contacts'),
]