# Generated by Django 3.0.6 on 2020-09-16 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200916_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='mediafile',
            field=models.FileField(upload_to='mediafiles/'),
        ),
    ]