# Generated by Django 3.2.4 on 2021-06-30 13:41

from django.db import migrations
import json
from django.contrib.gis.geos import fromstr
from pathlib import Path

DATA_FILENAME = 'data.json'
def load_data(apps, schema_editor):
    Shop = apps.get_model('shops', 'Shop')
    jsonfile = Path(__file__).parents[2] / DATA_FILENAME

    with open(str(jsonfile)) as datafile:
        objects = json.load(datafile)
        for obj in objects['features']:
            try:
                objType = obj['type']
                if objType == 'Point':
                    name = name
                    longitude = obj.get('lon',0)
                    latitude = obj.get('lat', 0)
                    location = fromstr(f'POINT{longitude} {latitude})', srid=4326)
                    Shop(name=name, location = location).save()
            except KeyError:
                pass  

class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]
