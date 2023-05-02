from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request) :
    return HttpResponse("장고 게섯거라 이요환이 간다.")