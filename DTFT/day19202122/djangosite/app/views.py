#-*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import os
from app.forms import MomentForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
def welcome(request):
	return HttpResponse('<h1>Welcome to my tiny twitter!</h1>')
@csrf_exempt
# 作用是跳过 csrf 中间件的保护
def moments_input(request):
	if request.method == 'POST':
		form = MomentForm(request.POST)
		if form.is_valid():
			moment = form.save()
			moment.save()
			return HttpResponseRedirect(reverse('app.views.welcome'))
	else:
		form = MomentForm()
	PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	return render(request, os.path.join(PROJECT_ROOT, 'app/templates',
					'moments_input.html'), {'form' : form})