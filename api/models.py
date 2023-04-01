from django.db import models


class ObjectDetails(models.Model):
    image_name = models.CharField(max_length=250, null=True, blank=True)
    objects_detected = models.CharField(max_length=250, null=True, blank=True)
    timestamp = models.CharField(max_length=250, null=True, blank=True)
