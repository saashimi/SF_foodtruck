from django.contrib.gis.db import models

class Cart_db_data(models.Model):
    noisent = models.CharField(max_length=500)
    fooditems = models.CharField(max_length=500)
    facilitytype = models.CharField(max_length=500)
    received = models.DateField(null=True, blank=True)
    locationdescription = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    #:@computed_region_bh8s_q3mv = models.CharField(max_length=500)
    expirationdate = models.DateTimeField(null=True, blank=True)
    dayshours = models.CharField(max_length=500)
    objectid = models.CharField(max_length=500)
    lot = models.CharField(max_length=500)
    location_city = models.CharField(max_length=500)
    #:@computed_region_rxqg_mtj9 = models.CharField(max_length=500)
    #:@computed_region_fyvs_ahh9 = models.CharField(max_length=500)
    latitude = models.CharField(max_length=500)
    applicant = models.CharField(max_length=500)
    priorpermit = models.CharField(max_length=500)
    approved = models.DateTimeField(null=True, blank=True)
    cnn = models.CharField(max_length=500)
    #:@computed_region_yftq_j783 = models.CharField(max_length=500)
    permit = models.CharField(max_length=500)
    blocklot = models.CharField(max_length=500)
    status = models.CharField(max_length=500)
    block = models.CharField(max_length=500)
    y = models.CharField(max_length=500)
    location_state = models.CharField(max_length=500)
    x = models.CharField(max_length=500)
    location_zip = models.CharField(max_length=500)
    #:@computed_region_p5aj_wyqh = models.CharField(max_length=500)
    location_address = models.CharField(max_length=500)
    schedule = models.CharField(max_length=500)
    longitude = models.CharField(max_length=500)
    geom = models.PointField()

    def __str__(self):
        return 'Loading data for: {0}'.format(self.applicant) 
