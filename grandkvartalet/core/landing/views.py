# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from grandkvartalet.app.contact.forms import ContactForm
from django.core.mail import EmailMessage
import mandrill

def landing_view(request):
	if request.POST:
		form = ContactForm(request.POST)
		if form.is_valid():
			contact = form.save()
			mandrill_client = mandrill.Mandrill('52ZxkH8p1ENIBq0x2vokkg')
			message = {
				'from_email': 'kontakt@grandkvartalet.no',
				'from_name': 'kontakt@grandkvartalet.no',
				'subject': 'Ny melding fra grandkvartalet.no',
				'to': [
					{
						'email': 'fer@skc.no',
						'name': 'Finn Erik Røed',
						'type': 'to',
					},
					{
						'email': 'jan@inter-eiendom.no',
						'name': 'Jan Hansen',
						'type': 'to'
					},
				],

				'text': u'Navn: {}\r\n\r\nEmail: {}\r\n\r\n{}'.format(contact.name, contact.email, contact.message)
			}
			result = mandrill_client.messages.send(message=message, async=True)
	return render(request, 'landing.jade')

def display_pdf(request, fileurl):
	with open(fileurl, 'r') as pdf:
		response = HttpResponse(pdf.read(), mimetype='application/pdf')
		return response
