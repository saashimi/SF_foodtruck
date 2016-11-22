# SF Foodtruck Locator Application

This is a web application inspired by an Uber code challenge. Namely, how to use
Socrata API data and display it so that a user can find foodtrucks in San Francisco
within a half-mile radius from an input location.

## Development Stack
This project uses PostgreSQL 9.5 and PostGIS for spatial lookups. The Django 1.10.3 
makes navigating the geographic data much easier, especially with gdal tools. Django-leaflet 0.19 is used for the frontend. 

## Screenshot
![alt tag](https://github.com/saashimi/SF_foodtruck/blob/dev/screenshot.gif)  

## Misc. Development Notes
[Used the following SF Socrata API endpoint](https://data.sfgov.org/Economy-and-Community/Mobile-Food-Facility-Permit/rqzj-sfat) and saved as .geojson.

Populated the PostgreSQL (and PostGIS-enabled) database with the [geodjango LayerMapping data import utility]:(https://docs.djangoproject.com/en/1.10/ref/contrib/gis/layermapping/)
```
$ python manage.py ogrinspect <filename>.geojson <model_name> --mapping

```
Created a python load script to extract all features and place them into the PostgreSQL database:
```python
def run(verbose=True):
    lm = LayerMapping(<"model name">, <".geojson file">, <"Layer Mapping Data">,
                      transform=False, encoding='utf-8') 
                  
    lm.save(strict=True, verbose=verbose)
```