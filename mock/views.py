from django.shortcuts import render

# Create your views here.
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from models import *
def database(request,name):
    try:
        p = Project.objects.get(name=name)
        return JsonResponse(p.to_obj(),safe=False)
    except:
        return JsonResponse(dict(
            error='no database found'
        ))
