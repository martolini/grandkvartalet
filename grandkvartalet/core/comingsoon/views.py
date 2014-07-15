from django.shortcuts import render

def comingsoon(request):
	return render(request, 'index.jade')
