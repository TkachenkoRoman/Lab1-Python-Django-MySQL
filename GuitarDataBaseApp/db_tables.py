import django_tables2 as tables

class Guitar_types(tables.Table):
    id = tables.Column()
    name  = tables.Column()
    class Meta:
        attrs = {"class": "paleblue"}


class Pickups(tables.Table):
    id = tables.Column()
    produser_id = tables.Column()
    type = tables.Column()
    set_type = tables.Column()
    class Meta:
        attrs = {"class": "paleblue"}