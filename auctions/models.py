from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Listing(models.Model):
    id = models.AutoField(primary_key=True)
    listing_title = models.CharField(max_length=30)
    listing_description = models.CharField(max_length=90)
    starting_bid = models.IntegerField()
    listing_image = models.URLField()