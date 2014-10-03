from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from db_methods import *
from db_tables import *
import django_tables2 as tables
from django.views.decorators.http import require_http_methods
from django.core.context_processors import csrf

def guitar_types_view(request):
    table = Guitar_types(generate_data("Guitar_types", ("id", "name")))
    return render(request, 'templates/base.html', {'mytable': table, 'filter':None, 'guitar_types': None, 'produsers': None})

def pickups_view(request):
    table = Pickups(generate_data("Pickups", ("id", "produser_id", "type", "set_type")))
    return render(request, 'templates/base.html', {'mytable': table, 'filter':None, 'guitar_types': None, 'produsers': None})

def produsers_view(request):
    table = Produser(generate_data("Produser", ("id", "name", "rating", "guitar", "bridge", "pickups", "info")))
    return render(request, 'templates/base.html', {'mytable': table, 'filter':None, 'guitar_types': None, 'produsers': None})

def bridge_view(request):
    table = Bridge(generate_data("Bridge", ("id", "name", "material", "color", "produser_id")))
    return render(request, 'templates/base.html', {'mytable': table, 'filter':None, 'guitar_types': None, 'produsers': None})

def body_view(request):
    table = Body(generate_data("Body", ("id", "material", "color", "type", "form")))
    return render(request, 'templates/base.html', {'mytable': table, 'filter':None, 'guitar_types': None, 'produsers': None})

def guitar_view(request):
    table = Guitar(generate_data("Guitar", ("id", "name", "string_amount", "price", "neck_material", "Fretboard_material", "Pick_guard", "Type_id", "Body_id", "Bridge_id", "Pickups_id", "Guitar_produser_id")))
    return render(request, 'templates/base.html', {'mytable': table, 'filter':None, 'guitar_types': get_guitar_types(), 'produsers': get_produsers()})

def index(request):
    table = Pickups(generate_data("Pickups", ("id", "produser_id", "type", "set_type")))
    return render(request, 'templates/base.html',{'mytable': table, 'filter':None, 'guitar_types': None, 'produsers': None})

def edit_view(request, edit_id):
    #response = "You're clicked edit button with id %s."
    return render(request, 'templates/edit_form.html', {"action_url": "/Edit/confirm/", \
                                                        "title": "Edit Guitar", \
                                                        "guitar": get_guitar(edit_id), \
                                                        "guitar_type": get_guitar_type(edit_id),\
                                                        "guitar_types":get_guitar_types(),\
                                                        "body": get_body(edit_id), "bodies": get_bodies(),\
                                                        "bridge": get_bridge(edit_id), "bridges": get_bridges(),\
                                                        "pickup": get_pickup(edit_id), "pickups": get_pickups(),\
                                                        "produser": get_produser(edit_id), "produsers": get_produsers(),\
                                                        "pickguard": get_pickguard(edit_id)})

def add_view(request):
    return render(request, 'templates/add_form.html', {
                                                        "guitar_types":get_guitar_types(),\
                                                        "bodies": get_bodies(),\
                                                        "bridges": get_bridges(),\
                                                        "pickups": get_pickups(),\
                                                        "produsers": get_produsers(),\
                                                        })

#@require_http_methods(["POST"])
def add_confirm_view(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        insert_guitar(request.POST.get('name', False), request.POST.get('strings', False),\
                      request.POST.get('price', False), request.POST.get('neck_material', False),             \
                      request.POST.get('fretboard_material', False), request.POST.get('type_id', False),      \
                      request.POST.get('body_id', False), request.POST.get('bridge_id', False),\
                      request.POST.get('pickups_id', False), request.POST.get('produser_id', False),\
                      request.POST.get('pickguard', False))
    print "before redirect"
    return redirect('/Guitar/')

@require_http_methods(["POST"])
def edit_confirm_view(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        update_guitar(request.POST["id"], request.POST.get('name', False), request.POST.get('strings', False),\
                      request.POST.get('price', False), request.POST.get('neck_material', False),             \
                      request.POST.get('fretboard_material', False), request.POST.get('type_id', False),      \
                      request.POST.get('body_id', False), request.POST.get('bridge_id', False),\
                      request.POST.get('pickups_id', False), request.POST.get('produser_id', False),\
                      request.POST.get('pickguard', False))
    #table = Guitar(generate_data("Guitar", ("id", "name", "string_amount", "price", "neck_material", "Fretboard_material", "Pick_guard", "Type_id", "Body_id", "Bridge_id", "Pickups_id", "Guitar_produser_id")))
    return redirect('/Guitar/')

def delete_view(request, delete_id):
    del_guitar(delete_id)
    return redirect('/Guitar/')

def load_csv_view(request):
    reload_db_from_csv()
    return redirect('/Guitar/')

filter_all = []
filter_dict = {}
filter_price = []
filter_type = []
filter_produser = []

def filter_check(request):
    price_checkbox = request.GET.get('price', False)
    type_checkbox = request.GET.get('type', False)
    produser_checkbox = request.GET.get('produser', False)
    del filter_dict['price']
    del filter_dict['type']
    del filter_dict['produser']
    del filter_all[:]

    return redirect('/Guitar/')

def filter_view(request):
    c = {}
    c.update(csrf(request))
    price = request.GET.get('price_select', False)

    if price:
        filter_dict['price'] = price
        if price != '-':
            filter_price.append('price')
            filter_price.append(price)
            filter_all.append(filter_price)


    type = request.GET.get('type_select', False)
    if type:
        filter_dict['type'] = type
        if type != '-':
            filter_type.append('type')
            filter_type.append(type)
            filter_all.append(filter_type)

    produser = request.GET.get('produser_select', False)
    if produser:
        filter_dict['produser'] = produser
        if produser != '-':
            filter_produser.append('produser')
            filter_produser.append(produser)
            filter_all.append(filter_produser)

    table = Guitar(generate_data("Guitar", ("id", "name", "string_amount", "price", "neck_material", "Fretboard_material",\
                                            "Pick_guard", "Type_id", "Body_id", "Bridge_id", "Pickups_id",\
                                            "Guitar_produser_id"), filter_dict))
    return render(request, 'templates/base.html', {'mytable': table, 'filter':filter_all, 'guitar_types': get_guitar_types(), 'produsers': get_produsers()})
