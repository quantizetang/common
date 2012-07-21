from django.shortcuts import HttpResponse
from first.users.models import users

def index(request):
    html = "<H1>Users Page</H1>"
    return HttpResponse(html)