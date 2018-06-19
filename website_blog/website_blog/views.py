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
from .forms import LoginForm,RegForm
from django.contrib.auth.models import User
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
	if request.method=='POST':
		login_form=LoginForm(request.POST)
		if login_form.is_valid():
			user=login_form.cleaned_data['user']
			auth.login(request,user)
			return redirect(request.GET.get('from',reverse('home')))
	else:
		login_form=LoginForm()
	context={}
	context['login_form']=login_form
	return render(request,'blog/login.html',context)
    
def register(request):
	if request.method=='POST':
		reg_form=RegForm(request.POST)
		if reg_form.is_valid():
			username=reg_form.cleaned_data['username']
			password=reg_form.cleaned_data['password']
			email=reg_form.cleaned_data['email']
			user=User.objects.create_user(username,email,password)
			user.save()
			#user=User()
			#user.username=username
			#
			#user.set_password(password)
			user=auth.authenticate(username=username,password=password)
			auth.login(user)
			return redirect(request.GET.get('from',reverse('home')))
	else:
		reg_form=RegForm()
	context={}
	context['reg_form']=reg_form
	return render(request,'blog/register.html',context)