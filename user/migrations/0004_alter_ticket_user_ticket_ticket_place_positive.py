# Generated by Django 5.0.2 on 2024-03-06 14:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_alter_event_location_alter_eventlocation_name_and_more'),
        ('user', '0003_auto_20240305_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='ticket',
            constraint=models.CheckConstraint(check=models.Q(('place__gte', 0)), name='ticket_place_positive'),
        ),
    ]