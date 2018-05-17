from django.shortcuts import render,get_object_or_404,render_to_response
from .models import Blog,BlogType
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.template import loader
from django.core.paginator import Paginator
from django.db.models import Count
def blog_list(request):
	template=loader.get_template('blog/index.html')
	latest_blog_list=Blog.objects.order_by('-last_updated_time')[:6]
	context={
	'latest_blog_list':latest_blog_list,
	}
	context['blog_types']=BlogType.objects.annotate(blog_count=Count('blog'))
	blog_dates=Blog.objects.dates('created_time','month',order="DESC")
	blog_dates_dict={}
	for blog_date in blog_dates:
		blog_count=Blog.objects.filter(created_time__year=blog_date.year,
			created_time__month=blog_date.month).count()
		blog_dates_dict[blog_date]=blog_count
	context['blog_dates']=blog_dates_dict
	return HttpResponse(template.render(context,request))

def blog_list_all(request):
	template=loader.get_template('blog/blogs_all.html')
	blog_list=Blog.objects.order_by('-last_updated_time')
	page_num=request.GET.get('page',1)
	paginator=Paginator(blog_list,10)
	page_of_blogs=paginator.get_page(page_num)#判断页码有效性
	context={
	'blog_list':page_of_blogs,
	}
	current_page_num=page_of_blogs.number
	#page_range=[current_page_num-2,current_page_num-1,current_page_num,current_page_num+1,current_page_num+2]
	page_range=list(range(max(current_page_num-2,1),min((current_page_num+2),paginator.num_pages)+1))
	if page_range[0]-1>=2:
		page_range.insert(0,'...')
	if paginator.num_pages-page_range[-1]>=2:
		page_range.append('...')
	if page_range[0]!=1:
		page_range.insert(0,1)
	if page_range[-1]!=paginator.num_pages:
		page_range.append(paginator.num_pages)
	context['blog_types']=BlogType.objects.annotate(blog_count=Count('blog'))
	context['current_page_num']=current_page_num
	context['page_range']=page_range
	blog_dates=Blog.objects.dates('created_time','month',order="DESC")
	blog_dates_dict={}
	for blog_date in blog_dates:
		blog_count=Blog.objects.filter(created_time__year=blog_date.year,
			created_time__month=blog_date.month).count()
		blog_dates_dict[blog_date]=blog_count
	context['blog_dates']=blog_dates_dict
	return HttpResponse(template.render(context,request))

def blog_detail(request,blog_id):
	context={}
	blog=get_object_or_404(Blog,pk=blog_id)

	if not request.COOKIES.get('blog_%s_readed' % blog_id):
		blog.read_count+=1
		blog.save()

	context['blog']=blog
	context['previous_blog']=Blog.objects.filter(created_time__gt=blog.created_time).last()
	context['next_blog']=Blog.objects.filter(created_time__lt=blog.created_time).last()
	#return render(request,'blog/detail.html',{'blog_id':blog})
	response=render_to_response('blog/detail.html',context)
	#response.set_cookie('blog_%s_readed' % blog_id,'true',max_age=60,expires=datetime)
	response.set_cookie('blog_%s_readed' % blog_id,'true')
	return response

def blogs_with_type(request,blogs_type_pk):
	context={}
	blog_type=get_object_or_404(BlogType,pk=blogs_type_pk)
	blog_list=Blog.objects.filter(blog_type=blog_type)
	page_num=request.GET.get('page',1)
	paginator=Paginator(blog_list,10)
	page_of_blogs=paginator.get_page(page_num)
	current_page_num=page_of_blogs.number
	#page_range=[current_page_num-2,current_page_num-1,current_page_num,current_page_num+1,current_page_num+2]
	page_range=list(range(max(current_page_num-2,1),min((current_page_num+2),paginator.num_pages)+1))
	if page_range[0]-1>=2:
		page_range.insert(0,'...')
	if paginator.num_pages-page_range[-1]>=2:
		page_range.append('...')
	if page_range[0]!=1:
		page_range.insert(0,1)
	if page_range[-1]!=paginator.num_pages:
		page_range.append(paginator.num_pages)
	context['blog_list']=page_of_blogs
	context['blog_type']=blog_type
	context['current_page_num']=current_page_num
	context['page_range']=page_range

	#Blog_Type.objects.annotate(blog_count=Count('blog_blog'))#或者类型名的小写

	context['blog_types']=BlogType.objects.annotate(blog_count=Count('blog'))#或者类型名的小写
	'''
	blog_types=BlogType.objects.all()
	blog_type_list=[]
	for blog_type in blog_types:
		blgo_type.blog_count=Blog.objects.filter(blog_type=blog_type).count
		blog_types_list.append(blog_type)
	'''
	blog_dates=Blog.objects.dates('created_time','month',order="DESC")
	blog_dates_dict={}
	for blog_date in blog_dates:
		blog_count=Blog.objects.filter(created_time__year=blog_date.year,
			created_time__month=blog_date.month).count()
		blog_dates_dict[blog_date]=blog_count
	context['blog_dates']=blog_dates_dict
	return render_to_response('blog/blogs_with_type.html',context)


def blogs_with_date(request,year,month):
	context={}
	#blog_time=get_object_or_404(BlogType,pk=blogs_dates_pk)
	blog_list=Blog.objects.filter(created_time__year=year,
			created_time__month=month)
	page_num=request.GET.get('page',1)
	paginator=Paginator(blog_list,10)
	page_of_blogs=paginator.get_page(page_num)
	current_page_num=page_of_blogs.number
	#page_range=[current_page_num-2,current_page_num-1,current_page_num,current_page_num+1,current_page_num+2]
	page_range=list(range(max(current_page_num-2,1),min((current_page_num+2),paginator.num_pages)+1))
	if page_range[0]-1>=2:
		page_range.insert(0,'...')
	if paginator.num_pages-page_range[-1]>=2:
		page_range.append('...')
	if page_range[0]!=1:
		page_range.insert(0,1)
	if page_range[-1]!=paginator.num_pages:
		page_range.append(paginator.num_pages)
	context['blog_list']=page_of_blogs
	#context['blog_type']=blog_type
	context['current_page_num']=current_page_num
	context['page_range']=page_range

	#Blog_Type.objects.annotate(blog_count=Count('blog_blog'))#或者类型名的小写

	context['blog_types']=BlogType.objects.annotate(blog_count=Count('blog'))#或者类型名的小写
	'''
	blog_types=BlogType.objects.all()
	blog_type_list=[]
	for blog_type in blog_types:
		blgo_type.blog_count=Blog.objects.filter(blog_type=blog_type).count
		blog_types_list.append(blog_type)
	'''
	blog_dates=Blog.objects.dates('created_time','month',order="DESC")
	blog_dates_dict={}
	for blog_date in blog_dates:
		blog_count=Blog.objects.filter(created_time__year=blog_date.year,
			created_time__month=blog_date.month).count()
		blog_dates_dict[blog_date]=blog_count
	context['blog_dates']=blog_dates_dict
	return render_to_response('blog/blogs_with_type.html',context)
