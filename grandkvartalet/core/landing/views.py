from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from grandkvartalet.app.contact.forms import ContactForm

def landing_view(request):
	if request.POST:
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
	return render(request, 'landing.jade')

def display_pdf(request, fileurl):
	with open(fileurl, 'r') as pdf:
		response = HttpResponse(pdf.read(), mimetype='application/pdf')
		return response
