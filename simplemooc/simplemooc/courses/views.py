from django.shortcuts import render
from django.http import HttpResponse

from .models import Course

def index(request):
	courses = Course.objects.all()
	template_name = 'courses/index.html'
	context = {
		'courses': courses
	}

	return render(request, template_name, context)

def details(request, pk):
	course = Course.objects.get(pk=pk)
	context = {
		'course': course
	}
	template_name = 'courses/details.html'

	return render(request, template_name, context)