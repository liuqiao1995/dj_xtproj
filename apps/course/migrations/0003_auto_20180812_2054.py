# Generated by Django 2.0.7 on 2018-08-12 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_courseorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorder',
            name='istype',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='courseorder',
            name='status',
            field=models.IntegerField(),
        ),
    ]