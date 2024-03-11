# Generated on 2024-02-20 09:00 by Django 5.0.2.

from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        # Creating the 'News' model with fields.
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('short_desc', models.TextField(max_length=256)),
                ('full_link', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
