# Generated by Django 3.0 on 2020-05-28 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retreats', '0009_remove_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
