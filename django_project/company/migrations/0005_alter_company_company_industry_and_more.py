# Generated by Django 4.2.7 on 2023-12-02 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_alter_company_company_industry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_industry',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_mission',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]