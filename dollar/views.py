from django.shortcuts import render_to_response, render
from dollar.models import Subscriber


def home(request):
    render_to_response('home.html')

def subscribe(request):
    if request.method == 'POST':
        print(request.POST)
