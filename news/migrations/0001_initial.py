# Generated by Django 5.0.2 on 2024-03-13 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('short_desc', models.TextField(max_length=256)),
                ('full_link', models.TextField()),
                ('image', models.ImageField(upload_to='images/news/')),
            ],
            options={
                'verbose_name_plural': 'News',
            },
        ),
    ]
