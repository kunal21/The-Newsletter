from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from .forms import PostForm

def create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Succesfully Created")
	else:
		messages.error(request,"Not Succesfully Created")
	context = {
		"form":form,
			}
	return render(request,'post_form.html',context)

def detail(request,id=None):
	instance = Post.objects.get(id=id)
	context = {
		"instance":instance,
		"title":"User-Details"
		}
	return render(request,'post_details.html',context)

def list(request):
	queryset = Post.objects.all()
	context = {
		"object_list":queryset,
		"title":"List"
	}
	return render(request,'base.html',context)

def update(request,id=None):
	instance = Post.objects.get(id=id)
	form = PostForm(request.POST or None,instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		#return HttpResponseRedirect(instance.)
	context = {
		"title":instance.title,
		"form":form,
		"instance":instance,
	}
	return render(request,'post_form.html',context)
	

def delete(request,id=None):
	instance = Post.objects.get(id=id)
	instance.delete()
	return redirect("posts:list")