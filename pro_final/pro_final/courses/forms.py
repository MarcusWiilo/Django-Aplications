from django import forms
from django.proedu.mail import send_mail

class ContactCourse(forms.Form):

	name = forms.CharField(label='Nome', max_length=100)
	email = forms.EmailField(label='E-mail')
	message = forms.CharField(label='Mensagem/Dúvida', widget=forms.Textarea)

	def send_mail(self, course):
		subject = 'Contato sobre o curso %s' % course