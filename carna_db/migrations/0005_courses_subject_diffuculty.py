# Generated by Django 3.2.3 on 2021-05-22 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carna_db', '0004_match_example'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='subject_diffuculty',
            field=models.CharField(default=' ', max_length=30),
            preserve_default=False,
        ),
    ]
