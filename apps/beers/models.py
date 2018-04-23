from django.db import models
from django_countries.fields import CountryField


class BeerGenre(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name


class Beer(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, blank=True, null=True)
    picture = models.ImageField(
        upload_to="beersImages", default="beersImages/default.png")
    website = models.URLField(blank=True, null=True)
    genre = models.ForeignKey(BeerGenre, on_delete=models.DO_NOTHING)
    country = CountryField(blank_label='(select country)')

    def __str__(self):
        return self.name
