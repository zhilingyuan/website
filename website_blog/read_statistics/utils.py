import datetime
from django.contrib.contenttypes.models import ContentType
from .models import Read_Count,Read_Detail
from django.utils import timezone
from django.db.models import Sum,Count
def read_statistic_once_read(request,obj):
	ct=ContentType.objects.get_for_model(obj)
	key="%s_%s_read" % (ct.model,obj.id)
	if not request.COOKIES.get(key):
		read_count,created=Read_Count.objects.get_or_create(content_type=ct,object_id=obj.id)
		read_count.read_count+=1
		read_count.save()
		date=timezone.now().date()
		read_detail,created=Read_Detail.objects.get_or_create(content_type=ct,object_id=obj.id,date=date)
		read_detail.read_num+=1
		read_detail.save()
	return key

def get_seven_days_read_data(content_type):
	today=timezone.now().date()
	read_num_list=[]
	dates_list=[]
	for _ in range(7,-1,-1):
		date=today-datetime.timedelta(days=_)
		dates_list.append(date.strftime('%m/%d'))
		read_details=Read_Detail.objects.filter(content_type=content_type,date=date)
		result=read_details.aggregate(read_num_sum=Count('read_num'))
		read_num_list.append(result['read_num_sum'])
	return dates_list,read_num_list

def get_today_hot_data(content_type):
	today=timezone.now().date()
	read_hot_list=[]
	read_details=Read_Detail.objects.filter(content_type=content_type,date=today).order_by('-read_num')[:2]
	return read_details

def get_yesterday_hot_data(content_type):
	yesterday=timezone.now().date()-datetime.timedelta(days=1)
	read_hot_list=[]
	read_details=Read_Detail.objects.filter(content_type=content_type,date=yesterday).order_by('-read_num')[:2]
	return read_details

def get_seven_days_hot_data(content_type):
	today=timezone.now().date()
	sevendate=timezone.now().date()-datetime.timedelta(days=7)
	read_details=Read_Detail.objects.filter(content_type=content_type,date__lte=today,date__gt=sevendate)\
							.annotate(read_num_sum=Sum('read_num'))\
							.order_by('-read_num_sum')[:2]
	return read_details
	