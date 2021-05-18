# Generated by Django 3.1.5 on 2021-05-15 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_db', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='id',
        ),
        migrations.AlterField(
            model_name='users',
            name='user_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='users',
            table='Users',
        ),
    ]