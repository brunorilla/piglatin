from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def translate(request):
	request.GET['origin']
	return render(request, 'translation.html')	