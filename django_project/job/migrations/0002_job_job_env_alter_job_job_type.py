# Generated by Django 4.2.7 on 2023-12-02 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_env',
            field=models.CharField(blank=True, choices=[('Remote', 'Remote'), ('In-Person', 'In-Person'), ('Hybrid', 'Hybrid')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(blank=True, choices=[('3-Months', '3-Months'), ('4-Months', '4-Months'), ('6-Months', '6-Months'), ('Contract', 'Contract')], max_length=20, null=True),
        ),
    ]
