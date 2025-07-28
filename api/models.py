from django.db import models
from django.utils.timezone import now, timedelta

class ShortURL(models.Model):
    original_url = models.URLField()
    shortcode = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expiry = models.DateTimeField()

class Click(models.Model):
    shorturl = models.ForeignKey(ShortURL, on_delete=models.CASCADE, related_name='clicks')
    timestamp = models.DateTimeField(auto_now_add=True)
    referrer = models.URLField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
