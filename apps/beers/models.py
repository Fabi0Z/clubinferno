from django.db import models


class Beer(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=1000)
    picture = models.ImageField(upload_to="beersImages")
    website = models.URLField()
