# Generated by Django 3.0.5 on 2020-05-03 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200503_0947'),
    ]

    operations = [
        migrations.RenameField(
            model_name='farmerprofile',
            old_name='farm_city',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='farmerprofile',
            old_name='farm_state',
            new_name='state',
        ),
        migrations.RenameField(
            model_name='farmerprofile',
            old_name='farm_street',
            new_name='street',
        ),
        migrations.RenameField(
            model_name='farmerprofile',
            old_name='farm_zipcode',
            new_name='zipcode',
        ),
    ]