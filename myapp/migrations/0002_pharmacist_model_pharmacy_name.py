# Generated by Django 5.1.3 on 2024-11-27 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pharmacist_model',
            name='Pharmacy_Name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]