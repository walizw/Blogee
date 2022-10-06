from django.db import models
from django.utils import timezone

class Category (models.Model):
    name = models.CharField (max_length=256)
    blog = models.DecimalField (max_digits=10, decimal_places=0) # The blog id that this category belongs to

    # Optional Fields
    parent_id = models.DecimalField (max_digits=10, decimal_places=0, default=-1)
    about = models.TextField (blank=True, null=True)
    icon = models.FileField (upload_to="cat_icons/", blank=True, null=True)
    posts = models.DecimalField (max_digits=10, decimal_places=0, default=0)
