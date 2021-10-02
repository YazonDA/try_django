from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
	print(f'request.path\n{request.path}')
	print(f'request.path_info\n{request.path_info}')
	print(f'request.scheme\n{request.scheme}')
	print(f'request.session\n{request.session}')
	print(f'request.upload_handlers\n{request.upload_handlers}')
	return HttpResponse("<h1>Hello people!</h1>")

def contact_view(request, *args, **kwargs):
	return HttpResponse("<h1>Contact page!</h1>")

def about_view(request, *args, **kwargs):
	return HttpResponse("<h1>About page!</h1>")

def social_view(request, *args, **kwargs):
	return HttpResponse("<h1>Social page!</h1>")
