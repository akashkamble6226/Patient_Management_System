# Generated by Django 3.0.5 on 2020-04-22 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0006_auto_20200422_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_patients',
            name='clinicalnotes',
            field=models.CharField(max_length=255, null=True),
        ),
    ]