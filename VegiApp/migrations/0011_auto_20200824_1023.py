# Generated by Django 3.0.3 on 2020-08-24 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VegiApp', '0010_authtokens'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Area',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='State',
        ),
    ]