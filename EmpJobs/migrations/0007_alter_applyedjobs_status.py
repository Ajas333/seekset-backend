# Generated by Django 5.0.4 on 2024-06-04 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmpJobs', '0006_applyedjobs_applyed_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyedjobs',
            name='status',
            field=models.CharField(choices=[('Application Send', 'Application Send'), ('Application Viewd', 'Application Viewd'), ('Resume Viewd', 'Resume Viewd'), ('Interview Sheduled', 'Interview Sheduled'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Application Send', max_length=20),
        ),
    ]