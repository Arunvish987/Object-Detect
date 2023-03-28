from django.shortcuts import render
from .models import ObjectDetails
from .serializers import ObjectDetailsSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import pandas as pd

api_view(['GET'])
def set_object_data(request):
    get_csv_files = request.FILES.get('key')
    get_file_data = pd.read_csv(get_csv_files)
    set_to_object = get_file_data.to_dict('records')
    serializer = ObjectDetailsSerializers(data=set_to_object,many=True)
    if serializer.is_valid():
        ObjectDetails.objects.bulk_create(**serializer)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_201_CREATED)







