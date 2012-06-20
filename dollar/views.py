from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from dollar.models import Subscriber
import pprint


def home(request):
    return render_to_response('home.html')

def subscribe(request):
    if request.method == 'POST':
        print(request.POST)
        #HOW DO WE RETURN json like: "{result:1}"
        new_subscriber = Subscriber(email=request.POST['email'])
        new_subscriber.save()
        return HttpResponse('{result:1, email:%s}' % request.POST['email'])

    if request.method == 'GET':
        email=request.GET['email']
           
        print '\n'.join(dir(request))
        new_subscriber = Subscriber(email=email)
        new_subscriber.save()

        resp = HttpResponse('{"status":"fuckyeah", "email":email}', "application/json")
        print dir(resp)
        return resp
        #return HttpResponse('{result:1, email:%s}' % request.GET['email'], content_type="application/json")


