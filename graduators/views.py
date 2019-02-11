#these imports support the shortcut approach whic uses render compacted with template pull and HttpResponse
from django.shortcuts import render
from django.http import Http404

#these imports support the good ol way of loader and templates seen in def newname2 rendering events
from django.http import HttpResponse
from django.template import loader

from graduators.models import graduator
from events.models import event
# Create your views here.
#this view has got bugs
def home(request):
    return render(request, "fispy/index.html")

def newname(request):

    all_graduators = graduator.objects.all()
    context = { 'all_graduators' : all_graduators, }
    return render(request, 'graduators/graduatorsmanifest3.html',context )

def details(request, graduator_id):
    try:
        kaka = graduator.objects.get(id=graduator_id)

    except Exception as e:
        raise Http404("That Graduator does not exist")
    return render(request, 'graduators/graduatordetails.html', { 'kaka': kaka })

    '''1.create variable to hold the db result.kaka = graduator.objects.get(pk=graduator_id)
       2.load template = loader.get_template('graduators/graduatordetails.html')
    context = { 'kaka' : kaka }
    return HttpResponse(template.render(context, request))
    '''

def newname2(request):
        all_events = event.objects.all()
        template = loader.get_template('eventpage/eventmanifest.html')
        context = { 'all_events' : all_events, }
        return HttpResponse(template.render(context, request))
