from django.shortcuts import render_to_response, render
from django.template import RequestContext
from dollar.models import Subscriber


def home(request):
    return render_to_response('home.html', context_instance=RequestContext(request))

def subscribe(request):
    if request.method == 'POST':
        print(request.POST)
        return True
    if request.method == 'GET':
        print "WERE IN GETGETGET"
        print(request.GET)
        return True
