from django.views.generic import TemplateView
from .models import Cart_db_data

class MainPageView(TemplateView): 
    template_name =  'cart_data/index.html'

def load_all_data():
    returned = Cart_db_data.objects.all()
    print(len(returned))
    print(returned)
    return returned

#load_all_data()
