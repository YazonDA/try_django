from django.http import HttpResponse
from django.shortcuts import render


def HomeView(request, *args, **kwargs):
	# print(f'dir(request)\n{dir(request)}')
	print(f'request.scheme\n{request.scheme}')
	context = {}
	return render(request, "home.html", context)
	# return HttpResponse('<h1>HttpResponse</h1>')


def about_view(request, *args, **kwargs):
	print(f'\n{request}')
	context = {}
	return render(request, "about.html", context)
