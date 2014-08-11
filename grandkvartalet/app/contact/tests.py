from django.test import TestCase
from .forms import ContactForm

class ContactTest(TestCase):

	def test_valid_form(self):
		d = {'name': 'Martin Roed', 'email': 'msroed@gmail.com', 'phone': '+47 45 19 19 91', 'message': 'This is a test'}
		form = ContactForm(d)
		self.assertTrue(form.is_valid())

	def test_invalid_form(self):
		d = {'name': 'Martin Roed', 'email': '', 'phone': '+47 45 19 19 91', 'message': ''}
		form = ContactForm(d)
		self.assertFalse(form.is_valid())