from django.contrib.auth import authenticate
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.shortcuts import redirect
from django.conf import settings

# Create your views here.
def login(request):
    return TemplateResponse(request, 'login.html')

def home(request):
    return TemplateResponse(request, 'home.html')

@csrf_protect
def process_login(request):
	username = request.POST.get('email')
	password = request.POST.get('password')

	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			auth.login(request, user)
			return HttpResponse('success')
		else:
			return HttpResponse('cannot login')
	else:
		return HttpResponse('wrong credentials')

def logout(request):
	auth.logout(request)
	return redirect(settings.LOGIN_REDIRECT_URL)
