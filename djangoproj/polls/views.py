from django.shortcuts import render
from django.http import HttpResponse

def headline(request):
	return render(request,'index.html',{})



