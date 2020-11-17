from django.shortcuts import render
from django.http import HttpResponse, JsonResponse,FileResponse,HttpResponseRedirect
# Create your views here.

def funlife(request):
    return JsonResponse({"errcode": 00,"description": "Fun life coming!"})


def showtep(request):
    return render(request,'funlife/muban.html')