from db import *

class BaseModel(Model):
    class Meta:
        database = db

class AtaqueModel(BaseModel):
    codigo = CharField(primary_key=True)
    responsable = CharField()
    ciudad = CharField()
    fecha = CharField()
    detalles = CharField()
    valor_monetario = CharField()
    fallecidos = IntegerField()
    heridos = IntegerField()
    latitud = FloatField()
    longitud = FloatField()

db.create_tables([AtaqueModel])