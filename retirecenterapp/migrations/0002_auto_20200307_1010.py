# Generated by Django 2.2.4 on 2020-03-07 16:10

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('retirecenterapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='altcontact',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, help_text='User phone number', max_length=31),
        ),
    ]
