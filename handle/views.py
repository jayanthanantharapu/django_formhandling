from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from handle.models import usr
from handle.forms import UserForm
import sys

# Create your views here.
def formhandl(request):
	context = RequestContext(request)
	if request.method == "POST":
		usr_name_id = UserForm(data = request.POST)
		if usr_name_id.is_valid():
			users = usr_name_id.save()
		else:
			print usr_name_id
	else:
		usr_name_id = UserForm()
	return render_to_response('forms.html',{},context)