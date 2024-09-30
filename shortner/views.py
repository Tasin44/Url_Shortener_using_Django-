from django.shortcuts import render,redirect
import uuid #Imports the uuid module to generate unique identifiers.
from .models import Url #Imports the Url model from models.py.
from django.http import HttpResponse
# Imports the HttpResponse class from django.http. 
# This is used to send responses back to the browser.



def index(request):
    return render(request,'index.html')

def create(request):
    if request.method=='POST': #Checks if the request method is POST(meaning the user submitted a form).
       link = request.POST['link'] # Get the long URL from the form submission
       uid = str(uuid.uuid4())[:5] # Generate a unique identifier (first 5 characters)
       new_url = Url(link=link,uuid=uid)# Create a new Url object
       new_url.save()# Save it to the database
       return HttpResponse(uid)  # Return the shortened identifier as a response


def go(request,pk):
    url_details=Url.objects.get(uuid=pk)# Retrieve Url object based on UUID
    return redirect ('https://'+url_details.link)# Redirect to the original long URL
'''
go Function: 
This view redirects users from the shortened URL back to the original long URL:

It takes a parameter pk (the UUID).
Retrieves the corresponding Url object from the database using get().
Redirects users to the original long URL using redirect() function.


def index(request):
This view function renders an HTML template (index.html)
when a user accesses the root URL. 
This page typically contains a form for users to input their long URLs.
'''
