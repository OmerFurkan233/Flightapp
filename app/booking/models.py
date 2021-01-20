from django.db import models


class Flight(models.Model):
    deptAirport = models.CharField(max_length=100, null=True)
    arrAirport = models.CharField(max_length=100, null=True)
    duration = models.CharField(null=True, max_length=100)
    airline = models.CharField(max_length=20, null=True)
    price = models.CharField(max_length=100, null=True)
    deptCity = models.CharField(max_length=100, null=True)
    arrCity = models.CharField(max_length=100, null=True)
    deptHour = models.CharField(null=True, max_length=100)
    arrHour = models.CharField(null=True, max_length=100)

    def __str__(self):
        return self.deptAirport+" "+self.arrAirport+" "+self.duration+" "\
               +self.airline+" "+self.price+" "+self.deptCity+" "+self.arrCity+" "+self.deptHour+" "\
               +self.arrHour
