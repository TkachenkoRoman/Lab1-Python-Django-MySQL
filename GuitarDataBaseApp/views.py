from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from db_methods import *
from db_tables import *
import django_tables2 as tables
from django.views.decorators.http import require_http_methods
from django.core.context_processors import csrf

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

def edit_view(request, edit_id):
    #response = "You're clicked edit button with id %s."
    return render(request, 'templates/edit_form.html', {"guitar": get_guitar(edit_id)})

@require_http_methods(["POST"])
def edit_confirm_view(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        update_guitar(request.POST["id"], request.POST.get('name', False), request.POST.get('strings', False), request.POST.get('price', False), request.POST.get('neck_material', False), request.POST.get('fretboard_material', False))
    table = Guitar(generate_data("Guitar", ("id", "name", "string_amount", "price", "neck_material", "Fretboard_material", "Pick_guard", "Type_id", "Body_id", "Bridge_id", "Pickups_id", "Guitar_produser_id")))
    return redirect('/Guitar/')

def delete_view(request, delete_id):
    del_guitar(delete_id)
    return redirect('/Guitar/')