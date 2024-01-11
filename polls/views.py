from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, 지니킴스프로젝트에 온걸 환영해")

# Create your views here.
