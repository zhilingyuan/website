from django.contrib import admin
from .models import BlogType
from .models import Blog
# Register your models here.
class BlogTypeAdmin(admin.ModelAdmin):
	list_display=('id','type_name')

class BlogAdmin(admin.ModelAdmin):
	list_display=('title','blog_type','author','created_time','last_updated_time')

admin.site.register(Blog,BlogAdmin)
admin.site.register(BlogType,BlogTypeAdmin)