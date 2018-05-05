from django.shortcuts import render,get_object_or_404,render_to_response
from .models import Blog,BlogType
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.template import loader

def blog_list(request):
	template=loader.get_template('blog/index.html')
	latest_blog_list=Blog.objects.order_by('-last_updated_time')[:6]
	context={
	'latest_blog_list':latest_blog_list,
	}
	return HttpResponse(template.render(context,request))

def blog_detail(request,blog_id):
	context={}
	blog=get_object_or_404(Blog,pk=blog_id)
	context['blog']=blog
	#return render(request,'blog/detail.html',{'blog_id':blog})
	return render_to_response('blog/detail.html',context)

def blogs_with_type(request,blogs_type_pk):
	context={}
	blog_type=get_object_or_404(BlogType,pk=blogs_type_pk)
	context['blogs']=Blog.objects.filter(blog_type=blog_type)
	context['blog_type']=blog_type
	return render_to_response('blog/blogs_with_type.html',context)

