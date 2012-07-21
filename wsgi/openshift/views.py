#from django.shortcuts import HttpResponse
#from first.users.models import users

#def index(request):
#    html = "<H1>Users Page</H1>"
#    return HttpResponse(html)


import os
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('home/test.html')