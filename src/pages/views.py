from django.http import HttpResponse
from django.shortcuts import render


def HomeView(request, *args, **kwargs):
	context = {}
	return render(request, "home.html", context)


def about_view(request, *args, **kwargs):
	context = {}
	return render(request, "about.html", context)

def TempView(request, *args, **kwargs):
	context = {}
	return render(request, "stopgap.html", context)