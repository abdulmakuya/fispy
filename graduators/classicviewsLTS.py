#this views has the graduators and classic connections to the details view of each graduator
#also there is no validation on the graduators/id if one attempts to enter directly at browser url
#also the view functions are still using template render with http response return
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from graduators.models import graduator
from events.models import event
# Create your views here.
#this view has got bugs
def home(request):
    template = loader.get_template('fispy/index.html')
    return HttpResponse(template.render(request))

def newname(request):

    all_graduators = graduator.objects.all()
    template = loader.get_template('graduators/graduatorsmanifest3.html')
    context = { 'all_graduators' : all_graduators, }
    return HttpResponse(template.render(context, request))

def details(request, graduator_id):
    return HttpResponse("<h2>Details for graduator id:" + str(graduator_id) + "</h2>")

def newname2(request):
        all_events = event.objects.all()
        template = loader.get_template('eventpage/eventmanifest.html')
        context = { 'all_events' : all_events, }
        return HttpResponse(template.render(context, request))
