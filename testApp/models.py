from django.db import models




class TemperatureReading(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    #title = models.CharField(max_length=100, blank=True, default='')
    #code = models.TextField()
    #linenos = models.BooleanField(default=False)
    dateTime = models.IntegerField(db_index=True) #datetime as unixepoch gmt
    sensor = models.IntegerField(db_index=True)   # id of sensor
    temp = models.IntegerField()     # temp as temp in Kelvin * 100

    class Meta:
        ordering = ('created',)