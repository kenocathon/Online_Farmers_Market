# Generated by Django 3.0.5 on 2020-05-06 22:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_farmerprofile_farm_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='farmerprofile',
            options={'ordering': ('-went_public',)},
        ),
        migrations.AddField(
            model_name='farmerprofile',
            name='slug',
            field=models.SlugField(default='slug-field', max_length=250, unique_for_date='public'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='farmerprofile',
            name='status',
            field=models.CharField(choices=[('not public', 'Not Public'), ('public', 'Public')], default='not public', max_length=10),
        ),
        migrations.AddField(
            model_name='farmerprofile',
            name='went_public',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]