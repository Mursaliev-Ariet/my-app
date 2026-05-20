from django.contrib import admin
from .models import *
from django.utils.html import format_html
from .models import Client

from django.contrib import admin
from django.utils.html import format_html
from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_car')
    readonly_fields = ('car_preview',)

    def show_car(self, obj):
        if obj.car:
            return format_html(
                '<img src="{}" width="120">',
                obj.car.url
            )
        return "Нет фото"

    show_car.short_description = 'Машина'

    def car_preview(self, obj):
        if obj.car:
            return format_html(
                '<img src="{}" width="300">',
                obj.car.url
            )
        return "Нет фото"

    car_preview.short_description = 'Предпросмотр'
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Group)
admin.site.register(Homework)
admin.site.register(Subject)