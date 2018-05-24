from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.fields import exceptions
from django.contrib.contenttypes.models import ContentType
from read_statistics.models import Read_Count,Get_Read_Count_Method,Read_Detail
from django.contrib.contenttypes.fields import GenericRelation 
# Create your models here.
class BlogType(models.Model):
	type_name=models.CharField(max_length=15)
	def __str__(self):
		return self.type_name

class Blog(models.Model,Get_Read_Count_Method):
	title=models.CharField(max_length=50)
	blog_type=models.ForeignKey(BlogType,on_delete=models.CASCADE)
	content=RichTextUploadingField()
	read_details=GenericRelation(Read_Detail)
	#read_count=models.IntegerField(default=0)
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	created_time=models.DateTimeField(auto_now_add=True)
	last_updated_time=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.title
	
'''				
class Read_Count(models.Model):
	read_count=models.IntegerField(default=0)
	blog=models.OneToOneField(Blog,on_delete=models.CASCADE)
'''