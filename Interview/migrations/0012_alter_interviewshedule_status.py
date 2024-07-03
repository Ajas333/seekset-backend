# Generated by Django 5.0.4 on 2024-06-25 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Interview', '0011_alter_interviewshedule_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewshedule',
            name='status',
            field=models.CharField(choices=[('Upcoming', 'Upcoming'), ('Canceled', 'Canceled'), ('You missed', 'You missed'), ('Selected', 'Selected'), ('Rejected', 'Rejected')], default='Upcoming', max_length=20),
        ),
    ]