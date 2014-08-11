from django_ajax.decorators import ajax
from .forms import ContactForm

@ajax
def send_ajax(request):
	d = request.POST.copy()
	d['message'] = d['detail']
	del d['detail']
	form = ContactForm(d)
	content = ''
	if form.is_valid():
		form.save()
		content = "<div class='success-contact'><div class='text-msg'>Your email was sent!</div></div>"
	else:
		print form.errors
		content = "<div class='error-msg'>Invalid Email, please provide an correct email.</div>";
	return {'content': content}

