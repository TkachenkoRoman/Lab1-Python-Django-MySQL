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

class Produser(tables.Table):
    id = tables.Column()
    name = tables.Column()
    rating = tables.Column()
    guitar = tables.BooleanColumn()
    bridge = tables.BooleanColumn()
    pickups = tables.BooleanColumn()
    info = tables.Column()
    class Meta:
        attrs = {"class": "paleblue"}

class Bridge(tables.Table):
    id = tables.Column()
    name = tables.Column()
    material = tables.Column()
    color = tables.Column()
    produser_id = tables.Column()
    class Meta:
        attrs = {"class": "paleblue"}

class Body(tables.Table):
    id = tables.Column()
    material = tables.Column()
    color = tables.Column()
    type = tables.Column()
    form = tables.Column()
    class Meta:
        attrs = {"class": "paleblue"}

class Guitar(tables.Table):
    id = tables.Column()
    name = tables.Column()
    string_amount = tables.Column(verbose_name="strings")
    price = tables.Column()
    neck_material = tables.Column(verbose_name="neck")
    Fretboard_material = tables.Column(verbose_name="fretboard")
    Pick_guard = tables.Column(verbose_name="pickguard")
    Type_id = tables.Column(verbose_name="type")
    Body_id = tables.Column(verbose_name="body")
    Bridge_id = tables.Column(verbose_name="bridge")
    Pickups_id = tables.Column(verbose_name="pickups")
    Guitar_produser_id = tables.Column(verbose_name="produser")
    class Meta:
        attrs = {"class": "paleblue"}