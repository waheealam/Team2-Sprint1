# Generated by Django 2.2.4 on 2020-03-07 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retirecenterapp', '0003_apartment_apt_resident_assign_orders_ordercomment_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='aptFloor',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='aptRoomNum',
            field=models.IntegerField(),
        ),
    ]