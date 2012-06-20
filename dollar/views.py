from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from dollar.models import Subscriber


def home(request):
    return render_to_response('home.html')

def subscribe(request):
    if request.method == 'POST':
        print(request.POST)
        #HOW DO WE RETURN json like: "{result:1}"
        new_subscriber = Subscriber(email=request.POST['email'])
        new_subscriber.save()
        return HttpResponse('{result:1, email:%s}' % request.POST['email'])
    if request.method == 'GET': # GET WORKS!!!  it onlykinda works... no response is sent back
                                #but it alsod oesn't 500 error out
        print "WERE IN GETGETGET"
        email=request.GET['email']
        new_subscriber = Subscriber(email=email)

        abc = HttpResponse('{"status":"fuckyeah", "email":email}', "application/json")
        print type(abc)
        print dir(abc)
        new_subscriber.save()
        return abc
        #return HttpResponse('{result:1, email:%s}' % request.GET['email'], content_type="application/json")


