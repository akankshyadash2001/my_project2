from django.shortcuts import render
from django.http import HttpResponse
def Akankshya(request):
    return HttpResponse('<h1>How are you</h1>')


def Twinkle(request):
    return HttpResponse('<marquee>I am good</marquee>')

# Create your views here.
