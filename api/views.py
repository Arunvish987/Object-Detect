import os
import csv
import shutil
import pandas as pd
from django.db.models import Q
from django.conf import settings
from rest_framework import status 
from api.models import ObjectDetails
from django.http import HttpResponse
from rest_framework.response import Response
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from .serializers import ObjectDetailsSerializers
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt    
@api_view(['POST'])
def set_object_data(request):
    get_csv_files = request.FILES['files[]']
    get_file_data = pd.read_csv(get_csv_files)
    set_to_object = get_file_data.to_dict('records')
    serializer = ObjectDetailsSerializers(data=set_to_object,many=True)
    if serializer.is_valid():
        serializer.save()
        print('created')
        return Response(status=status.HTTP_201_CREATED)
    
@csrf_exempt
@api_view(['POST'])
def get_data_between_date(request): 
    url = request.get_host()
    from_date = request.data.get('from_date')
    to_date = request.data.get('to_date')
    all_image_path = r'/home/anwar/Practice/interviewt task/images'
    get_object = ObjectDetails.objects.filter(Q(timestamp__gte=from_date) & Q(timestamp__lte=to_date))
    print('get_object',len(get_object))
    object_data = []
    for each_obj in get_object:
        each_data = model_to_dict(each_obj)
        shutil.copy(f'{all_image_path}/{each_obj.image_name}',settings.MEDIA_ROOT)
        each_data['image_name'] ='http:'+url+ '/'+ os.listdir(all_image_path)[os.listdir(all_image_path).index(each_obj.image_name)]
        object_data.append(each_data)
    print(object_data)
    return Response(data=object_data)


@api_view(['POST'])
def generate_report(request):
    from_date = request.data.get('from_date')
    to_date = request.data.get('to_date')
    get_object_list = list(ObjectDetails.objects.filter(Q(timestamp=from_date) & Q(timestamp=to_date)).values_list('objects_detected',flat=True))
    counts = dict()
    for each_obj in (",".join(get_object_list)).split(','):
        counts[each_obj] = counts.get(each_obj, 0) + 1
    data = {
        'threat':list(counts.keys()),
        'occurance':list(counts.values())
    }
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="{filename}.csv"'.format(filename='report')
    writer = csv.writer(response)
    df = pd.DataFrame(data)
    writer.writerow([column for column in df.columns])
    writer.writerows(df.values.tolist())
    return response









