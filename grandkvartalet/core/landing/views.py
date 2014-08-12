from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from grandkvartalet.app.contact.forms import ContactForm
from django.core.mail import EmailMessage

def landing_view(request):
	if request.POST:
		form = ContactForm(request.POST)
		if form.is_valid():
			contact = form.save()
			email = EmailMessage('Ny epost fra grandkvartalet.no', 'Navn: %s \r\n\r\nEmail: %s\r\n\r\n%s' % (contact.name, contact.email, contact.message), to=[ 'jan@inter-eiendom.no', 'fer@skc.no'])
			email.send()
	return render(request, 'landing.jade')

def display_pdf(request, fileurl):
	with open(fileurl, 'r') as pdf:
		response = HttpResponse(pdf.read(), mimetype='application/pdf')
		return response
