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
    path('mobile-development/', MobilPageView.as_view(), name='mobile'),

    path('design/', DesignPageView.as_view(), name='design'),
    path('marketing/', MarketingPageView.as_view(), name='marketing'),

    path('contacts/', ContactsPageView.as_view(), name='contacts'),
]