from django.contrib import admin
# imports the admin module from the django.contrib package.

from .models import Url

admin.site.register(Url)
'''
explain:

Registers your Url model with the Django admin site. 
This line accomplishes the following:

(i)Makes Url Objects Accessible in Admin

(ii)Generates Default Admin Interface:
Django automatically generates a basic admin interface for your Url model. 
This includes:
A list view that displays all existing shortened URLs.
An add/edit view for creating new shortened URLs or modifying existing ones.
Details view that shows information about a specific shortened URL.
'''

