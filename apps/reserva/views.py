# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, render_to_response
from .forms import PropertyForm, ReservationForm
from .models import *
# Create your views here.

def index(request):
    return render(request, 'reserva/index.html')

'''''
def propiedadView(request):

    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('reserva:index')
    else:
            form = PropertyForm()
        
    return render(request, 'reserva/propiedades_form.html', {'formo':form})
'''''

def reservaView(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        
        dates_id = dict(request.POST)["dates"]
        dates = request.POST.get("dates")
       # print("hola")
        print(dates_id)
       # print(dates)
        prop = Property.objects.get(id=id)

        reservation = Reservation()
        reservation.property = prop
        reservation.total = prop.tariff * int(dates)
        
        #print(reservation.total)
        reservation.save()
        for date_id in dates_id:
                available_day = AvailableDay.objects.get(id=date_id)
                available_day.reservation = reservation
                available_day.save(force_update=True)
        
        return redirect('reserva:index')
    
def mostrarfiltroView(request):
        if request.method == 'POST':
                city_name = request.POST.get("ciudad")
                begin_date = request.POST.get("principio")
                end_date = request.POST.get("final")

                if begin_date and end_date:
                        reservation_dates = AvailableDay.objects.filter(date__range=(begin_date, end_date))
                else:
                        reservation_dates = AvailableDay.objects.all()
                
                #print(begin_date)
                #print(end_date)

                properties = []
                flag = 1
                for reservation_date in reservation_dates:
                        for building in properties:
                                if building.pk == reservation_date.property.pk:
                                        flag = 0
                                        break
                        if flag == 1:
                                properties.append(reservation_date.property)
                        else:
                                flag = 1
                

                if city_name:
                        properties = filter(lambda obj: obj.city.description == city_name, properties)
        else:
                properties = Property.objects.all()

        return render(request, "reserva/buildings.html", {'buildings': properties})


def filtroView(request):
        return render(request, "reserva/filter.html")


def days(request, propertyId):
    ps = Property.objects.all()
    p = Property.objects.get(id=propertyId)
    days = AvailableDay.objects.filter(property=p, reservation=None)
    #print(p)
    #print(p.id)
    return render_to_response('reserva/days.html', {'Properties': ps, 'Days': days, 'prop':p})
