from django.shortcuts import render,get_object_or_404,render_to_response
def home(request):
	context={}
	return render_to_response('home.html',context)
