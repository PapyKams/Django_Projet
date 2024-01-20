from django.db import models

class Prospect(models.Model):
    campaign = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255)
    civility = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    function = models.CharField(max_length=100)
    email = models.EmailField()
    linkedin_url = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    direct_line = models.CharField(max_length=50, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    siret = models.CharField(max_length=14, blank=True, null=True)
    address_street = models.CharField(max_length=255)
    address_zip = models.CharField(max_length=10)
    address_city = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    workforce = models.IntegerField(blank=True, null=True)
    revenue = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    naf_code = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.company_name
