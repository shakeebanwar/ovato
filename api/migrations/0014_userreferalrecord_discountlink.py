# Generated by Django 3.2.6 on 2021-09-22 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_userreferalrecord_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='userreferalrecord',
            name='discountlink',
            field=models.TextField(default=''),
        ),
    ]