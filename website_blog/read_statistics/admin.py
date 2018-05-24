from django.contrib import admin
from .models import Read_Count,Read_Detail
# Register your models here.
class Read_CountAdmin(admin.ModelAdmin):
	list_display=('read_count','content_object')

class Read_DetailAdmin(admin.ModelAdmin):
	"""docstring for """
	list_display=('read_num','content_object','date')

admin.site.register(Read_Detail,Read_DetailAdmin)
admin.site.register(Read_Count,Read_CountAdmin)