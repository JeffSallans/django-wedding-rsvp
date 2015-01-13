from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.conf import settings
from django.utils import timezone
from rsvp.models import Household
from rsvp.models import Person
from rsvp.models import Rsvp
import requests
import json
import pprint

# Create your views here.

#used to get all the html for rsvp
def index(request):

	template = loader.get_template('base.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def get_rsvp(request):

	response_data = {}
	response_data['household'] = {}

	if request.method == 'GET':

		#Get request data
		address = request.GET.get('address', 0)
		
		#Retreive household data
		get_query = Household.objects.filter(address_number = address)
		if get_query.exists():
			response_data['household'] = Household.objects.get(address_number = address)

	return json.dumps(response_data)

def get_rsvp_page(request):

	template = loader.get_template('updateRsvp.html')
	context = RequestContext(request, {
		'rsvpJson': get_rsvp(request)
	})
	return HttpResponse(template.render(context))

def save_rsvp(request):

	response_data = {}
	response_data['is_success'] = False

	if request.method == 'POST':
		
		#Get request data
		rsvp_id = request.POST.get('rsvp_id', 0)
		new_count = request.POST.get('count', 0)
		
		#Update RSVP
		rsvp = Rsvp.objects.get(id_rsvp = rsvp_id)
		rsvp.count = new_count
		rsvp.last_modified = timezone.now
		rsvp.save()

		#Mark result as success
		response_data['is_success'] = True

	return HttpResponse(json.dumps(response_data), content_type = "application/json")

def get_all_rsvp(request):

	response_data = {}
	response_data['households'] = Household.objects.all()

	return HttpResponse(json.dumps(response_data), content_type = "application/json")
