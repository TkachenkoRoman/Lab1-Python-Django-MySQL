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

def produsers_view(request):
    table = Produser(generate_data("Produser", ("id", "name", "rating", "guitar", "bridge", "pickups", "info")))
    return render(request, 'templates/base.html', {'mytable': table})

def bridge_view(request):
    table = Bridge(generate_data("Bridge", ("id", "name", "material", "color", "produser_id")))
    return render(request, 'templates/base.html', {'mytable': table})

def body_view(request):
    table = Body(generate_data("Body", ("id", "material", "color", "type", "form")))
    return render(request, 'templates/base.html', {'mytable': table})

def guitar_view(request):
    table = Guitar(generate_data("Guitar", ("id", "name", "string_amount", "price", "neck_material", "Fretboard_material", "Pick_guard", "Type_id", "Body_id", "Bridge_id", "Pickups_id", "Guitar_produser_id")))
    return render(request, 'templates/base.html', {'mytable': table})

def index(request):
    table = Pickups(generate_data("Pickups", ("id", "produser_id", "type", "set_type")))
    return render(request, 'templates/base.html',{'mytable': table})