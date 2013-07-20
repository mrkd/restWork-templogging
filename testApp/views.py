from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from testApp.models import TemperatureReading
from testApp.serializers import TemperatureReadingSerializer

def POST(self):
       # (...)
       return HttpResponse(json.dumps(True), mimetype="text/javascript")

class TemperatureReadingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TemperatureReading.objects.all()
    serializer_class = TemperatureReadingSerializer

#@csrf_exempt
def temperatureReadings_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        temperatureReadings = TemperatureReading.objects.all()
        serializer = TemperatureReadingSerializer(snippets, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TemperatureReadingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        else:
            return JSONResponse(serializer.errors, status=400)

#@csrf_exempt
def temperatureReadings_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        temperatureReading = TemperatureReading.objects.get(pk=pk)
    except TemperatureReading.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TemperatureReadingSerializer(snippet)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TemperatureReadingSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        else:
            return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        temperatureReading.delete()
        return HttpResponse(status=204)
