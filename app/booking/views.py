from django.shortcuts import render, HttpResponse,HttpResponseRedirect
from booking.models import Flight
from booking.forms import FlightForm
from django.core.paginator import Paginator, EmptyPage

def add_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse("Success!")
            return HttpResponseRedirect('/flights/')
    else:
        form = FlightForm()

    return render(request, 'add_flight.html', {'form': form})

def all_flights(request):
    flights_list = Flight.objects.all()

    p= Paginator(flights_list, 2)
    page_num = request.GET.get('page', 1)
    page = p.page(page_num)
    c = {'flights_list' : flights_list}
    return render(request, "newflights.html", c)

def flight_search(request):
    result_set = Flight.objects.filter(deptCity__contains='İstanbul')
    return HttpResponse(str(len(result_set))+"number of person who satisfied that.")

def search_form(request):
    return render(request, "search_form.html")

def search(request):
    errors = []
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        if q=='':
          errors.append('Enter a search term!')
        elif len(q) > 20:
          errors.append('Please enter at most 20 characters!')
        else:
          flights = Flight.objects.filter(deptAirport__icontains=q)
          return render(request, 'search_result.html', {'flights': flights, 'query': q})
    return render(request, 'search_form.html', {'errors': errors})