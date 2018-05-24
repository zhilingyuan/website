from django.contrib import admin
from .models import BlogType
from .models import Blog
#from .models import Read_Count
# Register your models here.
class BlogTypeAdmin(admin.ModelAdmin):
	list_display=('id','type_name')

class BlogAdmin(admin.ModelAdmin):
	list_display=('title','blog_type','get_read_count','author','created_time','last_updated_time')

#class  Read_CountAdmin(admin.ModelAdmin):
	"""docstring for  Read_CountAdmin"""
#	list_display=('read_count','blog')
		
admin.site.register(Blog,BlogAdmin)
admin.site.register(BlogType,BlogTypeAdmin)
#admin.site.register(Read_Count,Read_CountAdmin)