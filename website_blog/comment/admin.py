from django.contrib import admin
from .models import Comment
# Register your models here.
class CommentAdmin(admin.ModelAdmin):
	"""docstring for ClassName"""
	list_display=('content_object','text','comment_time','user')

admin.site.register(Comment,CommentAdmin)