from django.db import models
from datetime import date


class SponsorProvider(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name + " " + self.surname


class Sponsor(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=1000)
    picture = models.ImageField(upload_to="sponsorsImages")
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    showAnyway = models.BooleanField(
        "show this sponsor also if subscription is expired", default=False)
    last_payment = models.DateField(
        "last payment of the subscription", default=date.today)
    owner = models.ForeignKey(SponsorProvider, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
