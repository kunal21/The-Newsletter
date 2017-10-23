from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import certifi
#import mechanicalsoup
from . import forms

def newsletter_home_page(request):
	htmltext = urllib.request.urlopen("http://www.ndtv.com/topic/short/news")
	soup = BeautifulSoup(htmltext)
	news = []
	for i in soup.find_all('p',{"class":"intro"}):
		news.append(i.getText())
	return render(request,'newsletter_home_page.html',{'news':news})
	

def newsletter_espn(request):
	var = request.POST.getlist('sports')
	print(var)
	news = []
	image_src = []
	for i in var:	
		htmltext = urllib.request.urlopen(i)
		soup = BeautifulSoup(htmltext)
		for i in soup.find_all('p',{"class":"contentItem__subhead contentItem__subhead--story"}):
			news.append(i.getText())
		for image in soup.find_all('img'):
			print(image)
			image_src.append(image.get('data-default-src'))
			if image is None:
				image_src.pop(0)
	return render(request,'newsletter_espn.html',{'news':news,'image':image_src})
		
		
def newsletter_about(request):
	return render(request,'newsletter_about.html',{})

def newsletter_technology(request):
	return render(request,newsletter_technology.html,{})



	