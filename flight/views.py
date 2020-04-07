from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Flights, Passengers
from django.urls import reverse

# Create your views here.
def index(request):
    context = {
        'flights':Flights.objects.all()
    }
    return render(request, "flights/index.html", context)

def flight(request, flight_id):
    try:
        flight = Flights.objects.get(pk=flight_id)
    except Flights.DoesNotExist:
        raise Http404('Flight does not exist')
    context = {
        "flights":flight,
        "passengers":flight.passengers.all(),
        "non_passengers": Passengers.objects.exclude(flights=flight).all()
    }
    return render(request, "flights/flight.html", context)

def book(request, flight_id):
    try:
        passenger_id = int(request.POST["passenger"])
        passenger = Passengers.objects.get(pk=passenger_id)
        flight = Flights.objects.get(pk=flight_id)
    except KeyError:
        return render(request, "flights/error.html", {'message':'No Selection'})
    except Flights.DoesNotExist:
        return render(request, "flights/error.html", {'message':'No Flight'})
    except Passengers.DoesNotExist:
        return render(request, "flights/error.html", {'message': 'No Passengers'})

    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse("flight", args=(flight_id,)))
