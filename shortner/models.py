from django.db import models

# Create your models here

class Url(models.Model):
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=10)

'''
Explanation:
1.
(models.Model) which is a base class provided by Django's 
ORM system. By inheriting from models.Model, 
the Url class gains all the functionalities of a Django model, 
including the ability to interact with the database.

When you create a new model class by inheriting from models.Model, 
Django automatically generates the necessary database table structure 
based on the fields you define within the model class.


2.
This model has two fields:
link: A character field, It will store the original,long URL that needs to be shortened. 
uuid:It will store a unique identifier for each shortened URL. 
This identifier will be used to redirect users to the original URL when they visit the shortened one. 
'''