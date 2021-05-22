# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    studying_at_id=models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'Users'

class Courses(models.Model):
    coursename=models.CharField(max_length=30)
    subject =models.CharField(max_length=30) #it technical words work for engineering ,statistics,math .. etc
    publisher=models.CharField(max_length=30) # indivuduals can submit courses to admin then admin can publish udemy model
    subject_diffuculty=models.CharField(max_length=30)
    class Meta:
        db_table = 'Courses'

class Match_Example(models.Model):
    word=models.CharField(max_length=30)
    answer =models.CharField(max_length=30) #it arts  .. etc
    class Meta:
        db_table = 'Match_Example'

# Create your models here.
