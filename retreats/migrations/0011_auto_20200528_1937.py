# Generated by Django 3.0 on 2020-05-28 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retreats', '0010_auto_20200528_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='facilities',
            field=models.ManyToManyField(help_text='Select the Facilities Present', null=True, to='retreats.Facility'),
        ),
    ]