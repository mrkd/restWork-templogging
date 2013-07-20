from django.forms import widgets
from rest_framework import serializers
from testApp.models import TemperatureReading
#from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class TemperatureReadingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TemperatureReading
        fields = ('created', 'dateTime', 'sensor', 'temp')