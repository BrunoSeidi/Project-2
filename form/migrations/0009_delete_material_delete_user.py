# Generated by Django 4.1.1 on 2022-10-06 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0008_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Material',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
