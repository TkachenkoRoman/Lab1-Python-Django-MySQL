from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from gen_data import generate_data
from db_tables import *
import django_tables2 as tables

def guitar_types_view(request):
    table = Guitar_types(generate_data("Guitar_types", ("id", "name")))
    return render(request, 'templates/base.html', {'mytable': table})

def pickups_view(request):
    table = Pickups(generate_data("Pickups", ("id", "produser_id", "type", "set_type")))
    return render(request, 'templates/base.html', {'mytable': table})

def index(request):
    table = Pickups(generate_data("Pickups", ("id", "produser_id", "type", "set_type")))
    return render(request, 'templates/base.html',{'mytable': table})