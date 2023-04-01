from django.contrib import admin
from api.models import ObjectDetails


@admin.register(ObjectDetails)
class ObjectDetailsAdmin(admin.ModelAdmin):
    list_display = ['id','image_name','objects_detected','timestamp']
    
