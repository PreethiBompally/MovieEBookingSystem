# Generated by Django 4.1.6 on 2023-04-16 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_showtime_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
