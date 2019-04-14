# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'core/index.html')

def other(request):
	return render(request,'core/other.html')

def relative(request):
	return render(request,'core/relative_url_templates.html')		

def aboutus(request):
	return render(request,'core/aboutus.html')	