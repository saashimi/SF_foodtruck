from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core.serializers import serialize
from .models import Cart_db_data


class MainPageView(TemplateView): 
    template_name =  'cart_data/index.html'

def cart_db_data_view(request):
    cart_db_data_as_geojson = serialize('geojson', Cart_db_data.objects.all())
    return HttpResponse(cart_db_data_as_geojson, content_type='json')
