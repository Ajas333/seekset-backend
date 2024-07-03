# Generated by Django 5.0.4 on 2024-06-06 10:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmpJobs', '0007_alter_applyedjobs_status'),
        ('account', '0014_candidate_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyedjobs',
            name='status',
            field=models.CharField(choices=[('Application Send', 'Application Send'), ('Application Viewd', 'Application Viewd'), ('Resume Viewd', 'Resume Viewd'), ('Interview Sheduled', 'Interview Sheduled'), ('Interview Cancelled', 'Interview Cancelled'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Application Send', max_length=20),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='EmpJobs.jobs')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField()),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='account.candidate')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='EmpJobs.question')),
            ],
        ),
    ]