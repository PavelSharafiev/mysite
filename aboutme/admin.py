from django.contrib import admin

# Register your models here.
from aboutme.models import Slider, Skills, New


class SliderAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'text']}),
        ('Picture', {'fields': ['image']}),
    ]


class NewsAdmin(admin.ModelAdmin):
    fields = [
        'title', 'text', 'preview_image', 'pub_date'
    ]


admin.site.register(Slider, SliderAdmin)
admin.site.register(Skills)
admin.site.register(New, NewsAdmin)
