# Generated by Django 3.0.8 on 2020-07-04 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0009_auto_20200704_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showcasepost',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='gallery'),
        ),
    ]
