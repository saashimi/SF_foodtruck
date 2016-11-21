from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.contrib.gis.geos import fromstr
from django.contrib.gis.measure import D
from .models import Cart_db_data


class MainPageView(TemplateView): 
    template_name =  'cart_data/index.html'

"""
def cart_db_data_view(request):
    cart_db_data_as_geojson = serialize('geojson', Cart_db_data.objects.all())
    return HttpResponse(cart_db_data_as_geojson, content_type='json')
"""

def cart_db_data_view(request, radius=1609*.5):
    lat = request.GET.get('lat')
    lng = request.GET.get('lng')
    user_location = fromstr('POINT({0} {1})'.format(lng, lat))
    desired_radius = {'m' : radius}
    nearby_carts = Cart_db_data.objects.filter(
        geom__distance_lte=(user_location, D(**desired_radius)))
    cart_db_data_as_geojson = serialize('geojson', nearby_carts)
    return HttpResponse(cart_db_data_as_geojson, content_type='json')
