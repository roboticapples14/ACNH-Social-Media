# Generated by Django 3.0.8 on 2020-07-10 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0011_auto_20200704_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showcasepost',
            name='image',
            field=models.FileField(blank=True, upload_to='gallery'),
        ),
    ]