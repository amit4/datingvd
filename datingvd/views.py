from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
	HttpResponse('<h1>Main Page</h1>')

	