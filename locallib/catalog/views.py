from django.shortcuts import render

# Create your views here.
def index(request):
    from django.http import HttpResponse
    return HttpResponse("<center><h1>testing")