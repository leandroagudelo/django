from django.http import HttpResponseBadRequest
from django.shortcuts import render_to_response
from django.template import RequestContext
from polls.models import Poll


def home(request):
    result = {}

    name = "hernan"
    lastname = "diaz"

    result['name'] = name
    result['lastname'] = lastname
    result['query'] = Poll.objects.all()

    return render_to_response('home.html',result ,context_instance=RequestContext(request))


def save_poll(request):
    result = {}
    question = request.POST["question"]

    try:
        poll = Poll()
        poll.question = question
        poll.save()

        result["status"] = "SUCCESS"
        result["msg_status"] = "Su encuesta se ha creado satisfactoriamente"

    except Exception as error:
        result["status"] = "FAILURE"
        result["msg_status"] = "Error en la creacion"



    return render_to_response('home.html',result ,context_instance=RequestContext(request))
