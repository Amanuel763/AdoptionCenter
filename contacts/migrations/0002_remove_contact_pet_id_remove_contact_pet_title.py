# Generated by Django 4.0.2 on 2022-02-17 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='pet_id',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='pet_title',
        ),
    ]