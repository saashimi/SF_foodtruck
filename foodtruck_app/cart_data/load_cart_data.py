import os
from django.contrib.gis.utils import LayerMapping
from .models import Cart_db_data

# Auto-generated `LayerMapping` dictionary for Cart_db_data model
cart_db_data_mapping = {

    'noisent' : 'noisent',
    'fooditems' : 'fooditems',
    'facilitytype' : 'facilitytype',
    'received' : 'received',
    'locationdescription' : 'locationdescription',
    'address' : 'address',
    'expirationdate' : 'expirationdate',
    'dayshours' : 'dayshours',
    'objectid' : 'objectid',
    'lot' : 'lot',
    'location_city' : 'location_city',
    'latitude' : 'latitude',
    'applicant' : 'applicant',
    'priorpermit' : 'priorpermit',
    'approved' : 'approved',
    'cnn' : 'cnn',
    'permit' : 'permit',
    'blocklot' : 'blocklot',
    'status' : 'status',
    'block' : 'block',
    'y' : 'y',
    'location_state' : 'location_state',
    'x' : 'x',
    'location_zip' : 'location_zip',
    'location_address' : 'location_address',
    'schedule' : 'schedule',
    'longitude' : 'longitude',
    'geom' : 'POINT'
}
 
data = os.path.abspath(os.path.join(os.path.dirname(__file__), 'output.geojson'))

def run(verbose=True):
    lm = LayerMapping(Cart_db_data, data, cart_db_data_mapping,
                      transform=False, encoding='utf-8') #KS guess utf-8
                  
    lm.save(strict=True, verbose=verbose)