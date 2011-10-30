from django.db import models
from django.template.defaultfilters import slugify

class Player(models.Model):

    name = models.CharField(max_length=20)
    session = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name
