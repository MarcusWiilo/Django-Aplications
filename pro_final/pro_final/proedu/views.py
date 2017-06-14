from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, 'home.html')
	
def contact(request):
	return render(request, 'contact.html')

def contact2(request):
	return render(request, 'contact2.html')

def contact3(request):
	return render(request, 'contact3.html')