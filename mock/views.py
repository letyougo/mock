from django.shortcuts import render

# Create your views here.
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from models import *

def database_list(request):
    return JsonResponse([p.to_obj() for p in Project.objects.all()],safe=False)

def database_item(request,id):
    try:
        p = Project.objects.get(id=id)
        return JsonResponse(p.to_obj(),safe=False)

    except:
        return JsonResponse(dict(
            error='no database found'
        ))

def table_list(request):
    return JsonResponse([t.to_obj() for t in Table.objects.all()],safe=False)

def table_item(request,id):
    try:
        t = Table.objects.get(id=id)
        return JsonResponse(t.to_obj(),safe=False)
    except:
        return JsonResponse(dict(
            error='no table found'
        ))