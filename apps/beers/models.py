from django.db import models


class BeerGenre(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name


class Beer(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, blank=True, null=True)
    picture = models.ImageField(upload_to="beersImages", blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    genre = models.ForeignKey(BeerGenre, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
