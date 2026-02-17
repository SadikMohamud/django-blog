from django.shortcuts import render
from django.http import HttpResponse

#create your views here.
def hello_blog(request):
    return HttpResponse("Hello, Blog!")
