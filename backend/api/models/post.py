from django.db import models
from django.utils import timezone

class Post (models.Model):
    # Required fields
    name = models.CharField (max_length=256)
    blog = models.DecimalField (max_digits=10, decimal_places=0) # The blog id that this post belongs to
    content = models.TextField ()

    # Optional fields
    author = models.DecimalField (max_digits=10, decimal_places=0, default=-1) # User id that posted this
    lang = models.CharField (max_length=12, default="en")

    slug = models.CharField (max_length=256, blank=True, null=True)
    date = models.DateTimeField (default=timezone.now)
    thumbnail = models.FileField (upload_to="thumbs/", blank=True, null=True)

    draft = models.BooleanField (default=False) # If this is a draft, it should not be public then

    tags = models.TextField (blank=True, null=True) # Format: tag1,tag2,tag3
    category = models.DecimalField (max_digits=10, decimal_places=0, default=0) # Category id

    views = models.DecimalField (max_digits=10, decimal_places=0, default=0)
    likes = models.DecimalField (max_digits=10, decimal_places=0, default=0)
    comments = models.DecimalField (max_digits=10, decimal_places=0, default=0)

    # These fields can be changed only by staff members or a superuser
    featured = models.BooleanField (blank=True, default=False)
    pinned = models.BooleanField (blank=True, default=False) # If pinned, this will be always be the first post in home
