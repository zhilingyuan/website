from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models.fields import exceptions
from django.utils import timezone
# Create your models here.
class Read_Count(models.Model):
	read_count=models.IntegerField(default=0) 
	content_type=models.ForeignKey(ContentType,on_delete=models.CASCADE)
	object_id=models.PositiveIntegerField()
	content_object=GenericForeignKey('content_type','object_id')

class Get_Read_Count_Method():
	"""docstring for get_read_count_times"""
	def get_read_count(self):
		try:
			ct=ContentType.objects.get_for_model(self)
			read_type_content=Read_Count.objects.get(content_type=ct,object_id=self.pk) 
			return read_type_content.read_count
		except exceptions.ObjectDoesNotExist as e:
			return 0

class Read_Detail(models.Model):
	"""docstring for Read_Detail"""
	date=models.DateField(default=timezone.now)
	read_num=models.IntegerField(default=0)

	content_type=models.ForeignKey(ContentType,on_delete=models.CASCADE)
	object_id=models.PositiveIntegerField()
	content_object=GenericForeignKey('content_type','object_id')

	
		
