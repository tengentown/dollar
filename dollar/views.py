from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from dollar.models import Subscriber


def home(request):
    return render_to_response('home.html')

def subscribe(request):
    if request.method == 'POST':
        print(request.POST)
        #HOW DO WE RETURN json like: "{result:1}"
        return HttpResponse('{result:1, email:%s}' % request.POST['email'])
    if request.method == 'GET': # GET WORKS!!!  it onlykinda works... no response is sent back
                                #but it alsod oesn't 500 error out
        print "WERE IN GETGETGET"
        return HttpResponse('{"town":1}', "application/json")
        #return HttpResponse('{result:1, email:%s}' % request.GET['email'], content_type="application/json")


