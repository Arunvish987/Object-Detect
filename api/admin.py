from django.contrib import admin
from api.models import ObjectDetails


admin.site.register(ObjectDetails)
class ObjectDetailsAdmin(admin.ModelAdmin):
    list_display = ['id','image_name','object_detected','time_stamp']
    
