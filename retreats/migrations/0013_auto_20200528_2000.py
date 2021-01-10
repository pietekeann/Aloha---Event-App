# Generated by Django 3.0 on 2020-05-28 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retreats', '0012_auto_20200528_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='picture_position',
            field=models.CharField(default='center', help_text='Type: up, down, or center to choose header image position ', max_length=6),
        ),
        migrations.AlterField(
            model_name='facility',
            name='name',
            field=models.CharField(max_length=500),
        ),
    ]