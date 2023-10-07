from django.contrib import admin
from authapp.models import CustomUser
from mainapp.models import (
    Category, Services, Reviews, Basket, WorkExample
)


@admin.register(CustomUser)
class AdminCustomUser(admin.ModelAdmin):
    pass


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    pass


@admin.register(Services)
class AdminServices(admin.ModelAdmin):
    pass


@admin.register(Reviews)
class AdminReviews(admin.ModelAdmin):
    pass


@admin.register(Basket)
class AdminBasket(admin.ModelAdmin):
    pass


@admin.register(WorkExample)
class AdminWorkExample(admin.ModelAdmin):
    pass
