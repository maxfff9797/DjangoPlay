from django.http import Http404,HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
import datetime
def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    current_date =datetime.datetime.now()
    return render_to_response('current_datetime.html',{'current_date':current_date})

def hours_ahead(request,offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404()
    dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
    return render_to_response('hours_ahead.html',{'current_date':current_date})

