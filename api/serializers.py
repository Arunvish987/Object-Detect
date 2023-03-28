from rest_framework import serializers
from .models import ObjectDetails

class ObjectDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ObjectDetails
        fields = ['id','image_name','object_detected','time_stamp']
