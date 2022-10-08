from django.db import models
from django.utils import timezone

class Blog (models.Model):
    # Required fields
    name = models.CharField (max_length=256)
    lang = models.CharField (max_length=12)

    # Optional fields
    author = models.DecimalField (max_digits=10,
                                  default=-1,
                                  decimal_places=0) # User id that this blog belongs to
    slug = models.CharField (max_length=256, blank=True, null=True)
    icon = models.FileField (upload_to="blog_icons/", blank=True, null=True)
    header_img = models.FileField (upload_to="blog_headers/", blank=True, null=True)
    creation_date = models.DateTimeField (default=timezone.now)
    about = models.TextField (blank=True, null=True)
