# Generated by Django 4.1.1 on 2022-10-03 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='commentary',
            field=models.TextField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='material',
            name='type',
            field=models.CharField(choices=[('M', 'Search with material'), ('SN', 'Search with serial number')], max_length=20),
        ),
    ]
