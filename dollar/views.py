from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from dollar.models import Subscriber
import json
import pretty

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
           
        #AHHHH... I DONT KNOW DJANGO AT ALL :(
        pretty.pprint(request.environ)
        new_subscriber = Subscriber(email=email)
        new_subscriber.save()

        result = pretty.pretty(request.environ)
        data={ "result": result,
               "email": email
        }
        data_as_json = json.dumps(data)        

        resp = HttpResponse(data_as_json, "application/json")
        print dir(resp)
        return resp
        #return HttpResponse('{result:1, email:%s}' % request.GET['email'], content_type="application/json")


