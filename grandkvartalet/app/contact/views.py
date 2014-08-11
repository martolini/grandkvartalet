from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .forms import ContactForm
from django.contrib import messages

def contact_view(request):
	if request.POST:
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Thank you for the message!")
		else:
			messages.success(request, "Something went wrong")
			print form.errors
	return redirect(reverse('landing'))

