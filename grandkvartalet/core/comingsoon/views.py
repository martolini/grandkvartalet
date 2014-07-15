from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .forms import SubscriberCreationForm

def comingsoon(request):
	if 'subscribed' not in request.session.keys():
		request.session['subscribed'] = False
	if 'email' not in request.session.keys():
		request.session['email'] = ''
	if request.POST:
		form = SubscriberCreationForm(request.POST)
		if form.is_valid():
			sub = form.save()
			request.session['subscribed'] = True
			request.session['email'] = sub.email
		else:
			print form.errors
	return render(request, 'index.jade', {'subscribed': request.session['subscribed'], 'sub_email': request.session['email']})

