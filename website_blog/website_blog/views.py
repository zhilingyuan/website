import datetime
from django.shortcuts import render,get_object_or_404,render_to_response,redirect
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from read_statistics.utils import get_seven_days_read_data,get_seven_days_hot_data,get_today_hot_data,get_yesterday_hot_data
from blog.models import Blog
from django.db.models import Sum
from django.core.cache import cache
from django.contrib import auth 
from django.urls import reverse
def get_seven_days_hot_blogs():
	today=timezone.now().date()
	date=today-datetime.timedelta(days=7)
	blogs=Blog.objects.filter(read_details__date__lte=today,read_details__date__gt=date)\
		   	  .values('id','title')\
		   	  .annotate(read_num_sum=Sum('read_details__read_num'))\
		   	  .order_by('-read_num_sum')
def home(request):
	context={}
	blog_content_type=ContentType.objects.get_for_model(Blog)
	dates,read_nums=get_seven_days_read_data(blog_content_type)
	today_hot_data=get_today_hot_data(blog_content_type)
	yesterday_hot_data=get_yesterday_hot_data(blog_content_type)
	seven_days_hot_data=get_seven_days_hot_data(blog_content_type)
	hot_blogs_for_seven_days=cache.get('hot_blogs_for_seven_days')
	if hot_blogs_for_seven_days is None:
		hot_blogs_for_seven_days=get_seven_days_hot_blogs()
		cache.set('hot_blogs_for_seven_days',hot_blogs_for_seven_days,3600)
	context['yesterday_hot_data']=yesterday_hot_data
	context['read_nums']=read_nums
	context['dates']=dates
	context['today_hot_data']=today_hot_data
	context['seven_days_hot_data']=seven_days_hot_data
	context['hot_blogs_for_seven_days']=get_seven_days_hot_blogs()
	return render(request,'home.html',context)
def login(request):
	username=request.POST.get('username','')#后面是获取不到为空
	password=request.POST.get('password','')
	user=auth.authenticate(request,username=username,password=password)
	referer=request.META.get('HTTP_REFRER',reverse('home'))
	if user is not None:
		auth.login(request,user)
		return redirect(referer)
	else:
		return render(request,'error.html',{'message':'用户名密码错误'})