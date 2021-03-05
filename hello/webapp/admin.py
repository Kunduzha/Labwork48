from django.contrib import admin
from webapp.models import Good
# Register your models here.


class GoodAdmin(admin.ModelAdmin):
    good_display=['id', 'name', 'price' 'category', ]
    list_filter=['category', 'name']
    search_fields=['name']
    fields=['id', 'name', 'price', 'description', 'remainder']
    readonly_fields=['id']


admin.site.register(Good, GoodAdmin)