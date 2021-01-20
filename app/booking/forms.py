from django import forms

from booking.models import Flight


class FlightForm(forms.ModelForm):
 class Meta:
  model = Flight
  fields = ['deptAirport','arrAirport','duration','airline','price','deptCity','arrCity','deptHour',
            'arrHour']
