# Generated by Django 2.2.4 on 2020-03-11 00:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('retirecenterapp', '0006_auto_20200307_1154'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Assign_Orders',
            new_name='Assign_Order',
        ),
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
    ]
