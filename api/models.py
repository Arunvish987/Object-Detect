from django.db import models


class ObjectDetails(models.Model):
    image_name = models.ImageField(upload_to="images/")
    object_detected = models.CharField(max_length=250, null=True, blank=True)
    time_stamp = models.CharField(max_length=250, null=True, blank=True)
