# Generated by Django 3.1.5 on 2021-05-17 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_db', '0004_auto_20210517_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
