from django.shortcuts import render
from django.http import HttpResponse, JsonResponse,FileResponse
# Create your views here


def showAppMsg(request):
    return JsonResponse({"errcode": 402545,"description": "request method is wrong!"})
