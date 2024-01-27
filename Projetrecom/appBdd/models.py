from django.db import models

class Prospect(models.Model):
    campaign = models.CharField(max_length=255, null=True, blank=True)
    company_name = models.CharField(max_length=255)
    civility = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    function = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    linkedin_url = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    direct_line = models.CharField(max_length=255, null=True, blank=True)
    website = models.URLField(blank=True, null=True)
    siret = models.CharField(max_length=255, null=True, blank=True)
    address_street = models.CharField(max_length=255, null=True, blank=True)
    address_zip = models.CharField(max_length=255, null=True, blank=True)
    address_city = models.CharField(max_length=255, null=True, blank=True)
    department = models.CharField(max_length=255, null=True, blank=True)
    sector = models.CharField(max_length=255, null=True, blank=True)
    workforce = models.CharField(max_length=255, null=True, blank=True)
    revenue = models.CharField(max_length=255, null=True, blank=True)
    naf_code = models.CharField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.campaign = self.campaign[:100]
        self.company_name = self.company_name[:255]
        self.civility = self.civility[:50]
        self.first_name = self.first_name[:100]
        self.last_name = self.last_name[:100]
        self.function = self.function[:255]
        self.email = self.email[:255]
        self.phone = self.phone[:255]
        self.direct_line = self.direct_line[:255]
        self.siret = self.siret[:255]
        self.address_street = self.address_street[:255]
        self.address_zip = self.address_zip[:10]
        self.address_city = self.address_city[:255]
        self.department = self.department[:100]
        self.sector = self.sector[:300]
        self.workforce = self.workforce[:255]
        self.revenue = self.revenue[:255]
        self.naf_code = self.naf_code[:255]

        super(Prospect, self).save(*args, **kwargs)

    class Meta:
        db_table = 'prospect'

    def __str__(self):
        return self.campaign
