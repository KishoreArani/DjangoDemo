# Generated by Django 2.1.1 on 2018-10-01 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0008_auto_20181001_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribution_centre',
            name='Contact',
            field=models.CharField(max_length=20),
        ),
    ]