# Generated by Django 3.0.1 on 2019-12-30 16:53

from django.db import migrations

def create_data(apps, schema_editor):
    Customer = apps.get_model('customers', 'Customer')
    Customer(first_name="customer 0001", last_name='customer 0001', email='customer0001@gmail.com', phone='00000000', adress='customer 0000 adress', description='customer 0001 description').save()

class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data)
    ]