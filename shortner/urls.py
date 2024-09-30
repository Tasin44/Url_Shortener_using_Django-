from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('create',views.create,name='create'),
    path('<str:pk>',views.go,name='go')# Dynamic URL mapping for UUIDs
    # this is for creating dynamic url  
]

'''

urlpatterns = [ ... ]: 
Creates a list of URL patterns that Django will use to match incoming requests.

Individual URL Patterns:
path('', views.index, name='index'):
This pattern matches the root URL (/).
When a request is made to the root URL, Django will call the index view function.
The name='index' part assigns a name to this pattern. 
This name can be used in templates or other parts of your application to reference this URL.

path('create', views.create, name='create'):
This pattern matches the URL /create.
When a request is made to /create, Django will call the create view function.
This view is likely responsible for handling the creation of new shortened URLs.

path('<str:pk>', views.go, name='go'):
This pattern matches URLs of the form /pk, where pk is a string representing a unique identifier (the UUID).

The <str:pk> part is a URL parameter. 
It captures the value of the pk part of the URL and passes it as an argument to the go view function.

When a request is made to a URL like /abcde, Django will call the go view function with the pk value "abcde".
This view is likely responsible for redirecting users to the original URL associated with the given UUID.

'''