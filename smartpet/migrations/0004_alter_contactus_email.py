# Generated by Django 5.1.1 on 2024-09-27 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartpet', '0003_alter_contactus_uploded_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='Email',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
