# Generated by Django 5.1.3 on 2024-11-27 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_pharmacist_model_pharmacy_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicine_model',
            old_name='Name',
            new_name='Description',
        ),
        migrations.AddField(
            model_name='medicine_model',
            name='Medicine_Name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='medicine_model',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
