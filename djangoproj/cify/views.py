from django.shortcuts import render
from django.http import HttpResponse


def cifylogin(request):
	return render(request,'cifylogin.html',{})