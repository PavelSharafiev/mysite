from django.shortcuts import render

# Create your views here.
from django.views import generic

from aboutme.models import Slider, Skills, New


class IndexView(generic.ListView):
    template_name = 'aboutme/index.html'
    context_object_name = 'index_page'

    def get_queryset(self):
        return {
            'slider': Slider.objects.all(),
            'skills': Skills.objects.all(),
            'news'  : New.objects.order_by('pub_date')[:3],
        }
